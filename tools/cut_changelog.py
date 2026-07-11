#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHANGELOG_PATH = ROOT / "CHANGELOG.md"
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
HEADING_RE = re.compile(r"^## \[([^\]]+)\](?:\s*-\s*(\d{4}-\d{2}-\d{2}))?\s*$")


def read_changelog() -> str:
    return CHANGELOG_PATH.read_text(encoding="utf-8")


def write_changelog(text: str) -> None:
    CHANGELOG_PATH.write_text(text, encoding="utf-8")


def normalize_version(raw: str) -> str:
    version = raw.strip()
    if version.startswith("v") or version.startswith("V"):
        version = version[1:]
    if not VERSION_RE.fullmatch(version):
        raise ValueError(f"invalid version '{raw}'; expected semver like 0.1.0")
    return version


def split_sections(text: str) -> tuple[str, list[tuple[str, str | None, str]]]:
    lines = text.splitlines()
    preamble: list[str] = []
    sections: list[tuple[str, str | None, str]] = []
    current_name: str | None = None
    current_date: str | None = None
    current_body: list[str] = []

    def flush() -> None:
        nonlocal current_name, current_date, current_body
        if current_name is None:
            return
        body = "\n".join(current_body).strip("\n")
        sections.append((current_name, current_date, body))
        current_name = None
        current_date = None
        current_body = []

    for line in lines:
        match = HEADING_RE.match(line)
        if match:
            if current_name is None and preamble and preamble[-1] == "":
                preamble.pop()
            flush()
            current_name = match.group(1)
            current_date = match.group(2)
            continue
        if current_name is None:
            preamble.append(line)
        else:
            current_body.append(line)

    flush()
    preamble_text = "\n".join(preamble).rstrip() + "\n\n"
    return preamble_text, sections


def render_sections(preamble: str, sections: list[tuple[str, str | None, str]]) -> str:
    chunks = [preamble.rstrip() + "\n"]
    for name, date, body in sections:
        heading = f"## [{name}]" if date is None else f"## [{name}] - {date}"
        chunks.append(heading)
        if body.strip():
            chunks.append("")
            chunks.append(body.rstrip())
        chunks.append("")
    return "\n".join(chunks).rstrip() + "\n"


def section_has_content(body: str) -> bool:
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("### "):
            continue
        if stripped.startswith("- "):
            return True
        return True
    return False


def find_section(
    sections: list[tuple[str, str | None, str]], name: str
) -> tuple[str, str | None, str]:
    for section in sections:
        if section[0] == name:
            return section
    raise ValueError(f"CHANGELOG.md has no section [{name}]")


def cut_version(version: str, release_date: str | None) -> None:
    version = normalize_version(version)
    date = release_date or dt.date.today().isoformat()
    preamble, sections = split_sections(read_changelog())

    for name, _, _ in sections:
        if name == version:
            raise ValueError(f"version [{version}] already exists in CHANGELOG.md")

    unreleased_name, _, unreleased_body = find_section(sections, "Unreleased")
    if not section_has_content(unreleased_body):
        raise ValueError("[Unreleased] has no entries to release")

    remaining = [section for section in sections if section[0] != "Unreleased"]
    empty_unreleased = (
        "Unreleased",
        None,
        "### Added\n\n### Changed\n\n### Fixed\n\n### Removed\n\n### Security",
    )
    new_sections = [empty_unreleased, (version, date, unreleased_body), *remaining]
    write_changelog(render_sections(preamble, new_sections))
    print(f"Cut CHANGELOG.md [Unreleased] -> [{version}] - {date}")


def extract_notes(version: str) -> str:
    version = normalize_version(version)
    _, sections = split_sections(read_changelog())
    _, date, body = find_section(sections, version)
    if not section_has_content(body):
        raise ValueError(f"[{version}] has no release notes content")

    title = f"## [{version}]" if date is None else f"## [{version}] - {date}"
    return f"{title}\n\n{body.strip()}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Cut or extract Keep a Changelog sections.")
    sub = parser.add_subparsers(dest="command", required=True)

    cut_parser = sub.add_parser("cut", help="move [Unreleased] into a versioned section")
    cut_parser.add_argument("--version", required=True, help="semver without leading v")
    cut_parser.add_argument("--date", help="YYYY-MM-DD (default: today)")

    extract_parser = sub.add_parser("extract", help="print notes for a version")
    extract_parser.add_argument("--version", required=True, help="semver without leading v")

    args = parser.parse_args()
    try:
        if args.command == "cut":
            cut_version(args.version, args.date)
        elif args.command == "extract":
            sys.stdout.write(extract_notes(args.version))
        else:
            raise ValueError(f"unknown command: {args.command}")
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
