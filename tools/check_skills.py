#!/usr/bin/env python3
from pathlib import Path
import re
import sys

import catalog_skills


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    def error(message: str) -> None:
        errors.append(f"ERROR: {message}")

    skill_dirs = sorted(p for p in ROOT.iterdir() if (p / "SKILL.md").is_file())
    skill_names = [p.name for p in skill_dirs]

    if not catalog_skills.check_readme():
        error("README.md skills catalog is out of date; run `make catalog`")

    for skill_dir in skill_dirs:
        skill = skill_dir.name
        path = skill_dir / "SKILL.md"
        text = read(path)
        lines = text.splitlines()
        rel_path = path.relative_to(ROOT)

        examples_path = skill_dir / "examples.md"
        reference_path = skill_dir / "reference.md"
        if not examples_path.is_file():
            error(f"{skill}/examples.md is required")
        elif not examples_path.read_text(encoding="utf-8").strip():
            error(f"{skill}/examples.md must not be empty")
        if not reference_path.is_file():
            error(f"{skill}/reference.md is required")
        elif not reference_path.read_text(encoding="utf-8").strip():
            error(f"{skill}/reference.md must not be empty")

        if not lines or lines[0] != "---":
            error(f"{rel_path} must start with YAML frontmatter")
            continue

        try:
            end = lines[1:].index("---") + 1
        except ValueError:
            error(f"{rel_path} missing closing frontmatter marker")
            continue

        frontmatter = "\n".join(lines[1:end])
        name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.MULTILINE)
        if not name_match:
            error(f"{rel_path} missing valid name field")
        elif name_match.group(1) != skill:
            error(f"{rel_path} name '{name_match.group(1)}' must match directory '{skill}'")

        desc_match = re.search(
            r"^description:\s*(?:>-\s*\n(?P<block>(?:\s{2,}.+\n?)+)|(?P<inline>.+))",
            frontmatter,
            re.MULTILINE,
        )
        if not desc_match:
            error(f"{rel_path} missing description")
        else:
            if desc_match.group("block") is not None:
                description = " ".join(line.strip() for line in desc_match.group("block").splitlines())
            else:
                description = desc_match.group("inline").strip()
            if not description:
                error(f"{rel_path} has empty description")
            if len(description) > 1024:
                error(f"{rel_path} description has {len(description)} chars; keep <= 1024")

        if len(lines) > 500:
            error(f"{rel_path} has {len(lines)} lines; keep SKILL.md under 500 lines")

        if f"[`{skill}`]({skill}/)" not in README:
            error(f"README.md missing skill table entry for {skill}")

        if "](examples.md)" not in text:
            error(f"{rel_path} must link to examples.md")
        if "](reference.md)" not in text:
            error(f"{rel_path} must link to reference.md")

        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in link or link.startswith("#") or link.startswith("mailto:"):
                continue
            target = (skill_dir / link).resolve()
            if not target.exists():
                error(f"{rel_path} links to missing file: {link}")

    badge_match = re.search(
        r"https://img\.shields\.io/badge/skills-(\d+)-brightgreen\.svg",
        README,
    )
    if not badge_match:
        error("README.md missing skills count badge")
    elif int(badge_match.group(1)) != len(skill_names):
        error(
            "README.md skills badge shows "
            f"{badge_match.group(1)} but repository has {len(skill_names)} skills"
        )

    for skill in skill_names:
        if skill_names.count(skill) > 1:
            error(f"duplicate skill name: {skill}")

    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", README):
        if "://" in link or link.startswith("#") or link.startswith("mailto:"):
            continue
        target = (ROOT / link).resolve()
        if not target.exists():
            error(f"README.md links to missing path: {link}")

    scan_roots = [
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / ".pre-commit-config.yaml",
        *ROOT.glob(".github/workflows/*.yml"),
        *ROOT.glob(".github/workflows/*.yaml"),
        *ROOT.glob("*/SKILL.md"),
        *ROOT.glob("*/reference.md"),
        *ROOT.glob("*/examples.md"),
    ]
    for template_dir in ROOT.glob("*/templates"):
        scan_roots.extend(p for p in template_dir.rglob("*") if p.is_file())

    absolute_path_pattern = re.compile(r"(/home/[^\s)]+|/Users/[^\s)]+)")
    for path in scan_roots:
        if not path.exists() or not path.is_file():
            continue
        text = read(path)
        rel_path = path.relative_to(ROOT)
        if not text.strip():
            error(f"{rel_path} must not be empty")
        for match in absolute_path_pattern.finditer(text):
            error(f"{rel_path} contains real user-specific absolute path: {match.group(1)}")

    for template in ROOT.glob("*/templates/*"):
        if template.is_file() and not read(template).strip():
            error(f"{template.relative_to(ROOT)} template must not be empty")

    if errors:
        print("\n".join(errors))
        return 1

    print("All skill checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
