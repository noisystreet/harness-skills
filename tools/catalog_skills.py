#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
BEGIN_MARKER = "<!-- BEGIN SKILLS CATALOG -->"
END_MARKER = "<!-- END SKILLS CATALOG -->"


@dataclass(frozen=True)
class Skill:
    name: str
    description: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = read(path).splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path.relative_to(ROOT)} must start with YAML frontmatter")

    try:
        end = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError(f"{path.relative_to(ROOT)} missing closing frontmatter marker") from exc

    frontmatter = lines[1:end]
    data: dict[str, str] = {}
    i = 0
    while i < len(frontmatter):
        line = frontmatter[i]
        if not line.strip():
            i += 1
            continue

        block_match = re.match(r"^([A-Za-z0-9_-]+):\s*>-\s*$", line)
        if block_match:
            key = block_match.group(1)
            i += 1
            values: list[str] = []
            while i < len(frontmatter) and frontmatter[i].startswith("  "):
                values.append(frontmatter[i].strip())
                i += 1
            data[key] = " ".join(values).strip()
            continue

        inline_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if inline_match:
            data[inline_match.group(1)] = inline_match.group(2).strip()
        i += 1

    return data


def load_skills() -> list[Skill]:
    skills: list[Skill] = []
    for skill_dir in sorted(p for p in ROOT.iterdir() if (p / "SKILL.md").is_file()):
        metadata = parse_frontmatter(skill_dir / "SKILL.md")
        name = metadata.get("name", "").strip()
        description = metadata.get("description", "").strip()
        if not name:
            raise ValueError(f"{skill_dir / 'SKILL.md'} missing name")
        if not description:
            raise ValueError(f"{skill_dir / 'SKILL.md'} missing description")
        skills.append(Skill(name=name, description=description))
    return skills


def escape_cell(value: str) -> str:
    return value.replace("\n", " ").replace("|", "\\|")


def render_catalog(skills: list[Skill]) -> str:
    lines = [
        "| Skill | Description |",
        "|-------|-------------|",
    ]
    for skill in skills:
        lines.append(
            f"| [`{skill.name}`]({skill.name}/) | {escape_cell(skill.description)} |"
        )
    return "\n".join(lines)


def replace_catalog(readme: str, catalog: str) -> str:
    pattern = re.compile(
        rf"{re.escape(BEGIN_MARKER)}\n.*?\n{re.escape(END_MARKER)}",
        re.DOTALL,
    )
    replacement = f"{BEGIN_MARKER}\n{catalog}\n{END_MARKER}"
    updated, count = pattern.subn(replacement, readme)
    if count != 1:
        raise ValueError(
            f"README.md must contain exactly one {BEGIN_MARKER} / {END_MARKER} block"
        )
    return updated


def expected_readme() -> str:
    return replace_catalog(readme=read(README_PATH), catalog=render_catalog(load_skills()))


def write_readme() -> None:
    README_PATH.write_text(expected_readme(), encoding="utf-8")


def check_readme() -> bool:
    current = read(README_PATH)
    expected = expected_readme()
    return current == expected


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the README skills catalog.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if README.md catalog is not up to date",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="rewrite README.md catalog in place",
    )
    args = parser.parse_args()

    if args.write:
        write_readme()
        print("Updated README.md skills catalog")
        return 0

    if args.check:
        if check_readme():
            print("README.md skills catalog is up to date")
            return 0
        print("README.md skills catalog is out of date; run `make catalog`", file=sys.stderr)
        return 1

    print(render_catalog(load_skills()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
