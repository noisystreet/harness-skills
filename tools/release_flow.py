#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import cut_changelog


ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, check=check, capture_output=False)


def run_capture(cmd: list[str]) -> str:
    result = subprocess.run(cmd, cwd=ROOT, text=True, check=True, capture_output=True)
    return result.stdout.strip()


def ensure_clean_worktree() -> None:
    status = run_capture(["git", "status", "--porcelain"])
    if status:
        raise ValueError("working tree is not clean; commit or stash first")


def ensure_gh() -> None:
    try:
        run(["gh", "--version"], check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise ValueError("`gh` is required for release-pr") from exc


def create_release_pr(version: str) -> None:
    version = cut_changelog.normalize_version(version)
    branch = f"release/v{version}"
    ensure_clean_worktree()
    ensure_gh()

    run(["git", "fetch", "origin"])
    run(["git", "checkout", "main"])
    run(["git", "pull", "--ff-only", "origin", "main"])
    existing = run_capture(["git", "branch", "--list", branch])
    if existing:
        raise ValueError(f"local branch {branch} already exists; delete it or choose another version")
    remote = subprocess.run(
        ["git", "ls-remote", "--exit-code", "--heads", "origin", branch],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if remote.returncode == 0:
        raise ValueError(f"remote branch origin/{branch} already exists")

    run(["git", "checkout", "-b", branch])
    cut_changelog.cut_version(version, release_date=None)
    run(["make", "check"])
    run(["git", "add", "CHANGELOG.md"])
    if not run_capture(["git", "diff", "--cached", "--name-only"]):
        raise ValueError("CHANGELOG.md unchanged after cut")
    run(["git", "commit", "-m", f"Release v{version}"])
    run(["git", "push", "-u", "origin", "HEAD"])

    body = f"""## Summary
- Cut `CHANGELOG.md` `[Unreleased]` into `## [{version}]`.
- After merge, run `make release-tag VERSION={version}` and push the tag to publish the GitHub Release.

## Test plan
- [ ] CI 通过
- [ ] After merge: `make release-tag VERSION={version}` then `git push origin v{version}`
"""
    run(
        [
            "gh",
            "pr",
            "create",
            "--base",
            "main",
            "--head",
            branch,
            "--title",
            f"Release v{version}",
            "--body",
            body,
        ]
    )
    print(f"Opened release PR for v{version} from {branch}")


def create_release_tag(version: str, *, push: bool) -> None:
    version = cut_changelog.normalize_version(version)
    tag = f"v{version}"
    ensure_clean_worktree()

    branch = run_capture(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    if branch != "main":
        raise ValueError(f"release-tag must run on main (current branch: {branch})")

    run(["git", "fetch", "origin"])
    run(["git", "pull", "--ff-only", "origin", "main"])
    local = run_capture(["git", "rev-parse", "HEAD"])
    remote = run_capture(["git", "rev-parse", "origin/main"])
    if local != remote:
        raise ValueError("local main is not aligned with origin/main")

    _, sections = cut_changelog.split_sections(cut_changelog.read_changelog())
    cut_changelog.find_section(sections, version)

    existing = subprocess.run(
        ["git", "rev-parse", "-q", "--verify", f"refs/tags/{tag}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if existing.returncode == 0:
        raise ValueError(f"tag {tag} already exists locally")

    remote_tag = subprocess.run(
        ["git", "ls-remote", "--exit-code", "--tags", "origin", tag],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if remote_tag.returncode == 0:
        raise ValueError(f"tag {tag} already exists on origin")

    run(["git", "tag", "-a", tag, "-m", tag])
    print(f"Created annotated tag {tag} at {local[:12]}")
    if push:
        run(["git", "push", "origin", tag])
        print(f"Pushed {tag}; GitHub Release workflow should run next")
    else:
        print(f"Publish with: git push origin {tag}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Protected-main release helpers.")
    sub = parser.add_subparsers(dest="command", required=True)

    pr_parser = sub.add_parser("pr", help="cut changelog on a release branch and open a PR")
    pr_parser.add_argument("--version", required=True)

    tag_parser = sub.add_parser("tag", help="create vVERSION tag on synced main")
    tag_parser.add_argument("--version", required=True)
    tag_parser.add_argument("--push", action="store_true", help="push the tag to origin")

    args = parser.parse_args()
    try:
        if args.command == "pr":
            create_release_pr(args.version)
        elif args.command == "tag":
            create_release_tag(args.version, push=args.push)
        else:
            raise ValueError(f"unknown command: {args.command}")
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: command failed: {' '.join(exc.cmd)}", file=sys.stderr)
        return exc.returncode or 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
