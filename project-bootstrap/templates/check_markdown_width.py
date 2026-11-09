#!/usr/bin/env python3
"""Check that Markdown prose respects a maximum display width.

CJK and other fullwidth characters count as two columns so the limit matches
what an editor or terminal renders. Keeping prose short makes diffs readable
and stops agent-facing docs from turning into very long single lines.

Skipped content: YAML frontmatter, fenced code blocks, table rows, and lines
that are only a badge, image, link, or bare URL. A line that exceeds the limit
only because of an unbreakable URL is allowed up to the hard limit.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

DEFAULT_MAX_WIDTH = 120
DEFAULT_HARD_WIDTH = 300
URL_PATTERN = re.compile(r"https?://\S+")
SINGLE_LINK_PATTERN = re.compile(
    r"^(?:"
    r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)"  # badge
    r"|!\[[^\]]*\]\([^)]*\)"  # image
    r"|\[[^\]]+\]\([^)]*\)"  # single link
    r"|<https?://[^>]+>"  # autolink
    r"|https?://\S+"  # bare URL
    r")$"
)


def display_width(value: str) -> int:
    return sum(2 if unicodedata.east_asian_width(char) in "WF" else 1 for char in value)


def check_file(path: Path, max_width: int, hard_width: int) -> list[str]:
    problems: list[str] = []
    in_frontmatter = False
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if number == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue
        if stripped.startswith("|") or SINGLE_LINK_PATTERN.match(stripped):
            continue
        width = display_width(line)
        if width <= max_width:
            continue
        if width <= hard_width and display_width(URL_PATTERN.sub("", line)) <= max_width:
            continue
        problems.append(f"{path}:{number}: line is {width} columns (max {max_width})")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Markdown line widths.")
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="files to check; defaults to every *.md below the current directory",
    )
    parser.add_argument("--max-width", type=int, default=DEFAULT_MAX_WIDTH)
    parser.add_argument("--hard-width", type=int, default=DEFAULT_HARD_WIDTH)
    args = parser.parse_args()

    root = Path.cwd()
    files = args.files or sorted(
        path for path in root.rglob("*.md") if ".git" not in path.relative_to(root).parts
    )
    problems = [problem for path in files for problem in check_file(path, args.max_width, args.hard_width)]
    if problems:
        print("\n".join(problems), file=sys.stderr)
        print(
            f"{len(problems)} Markdown line(s) exceed {args.max_width} columns; "
            "wrap the prose.",
            file=sys.stderr,
        )
        return 1
    print(f"Markdown line widths OK ({len(files)} file(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
