# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project uses semantic versioning when releases are created.

## [Unreleased]

### Added

- Added `migration`, `data-modeling`, and `release` skills with examples.
- Expanded ADR guidance in `docs-style`, concurrency rules in `clean-code` and language styles, and feature-flag cutover rules in `runtime-reliability`.
- Added `observability`, `performance`, `dependency-management`, and `refactoring` skills with examples.
- Added `make help` as the default Makefile target listing available commands.
- Added examples for `secure-coding` and `ci-quality`.
- Expanded `project-bootstrap` templates with CONTRIBUTING, CHANGELOG, env example, EditorConfig, pre-commit, and GitHub Actions CI starters.
- Added Makefile targets for Trae global skill install: `install-trae`, `install-trae-cn`, and matching list/uninstall commands.
- Added reference guides for `clean-code`, `rust-style`, `cpp-style`, and `python-style`.
- Added `make catalog` to regenerate the README skills catalog from `SKILL.md` metadata.
- Added repository `.pre-commit-config.yaml` with generic file checks, private key detection, and `make check`.
- Added GitHub Actions CI workflow for `make check`, checker compilation, and pre-commit.
- Added `CONTRIBUTING.md` with skill authoring and validation guidance.
- Added examples for `api-design` and `runtime-reliability`.
- Initialized this directory as a git repository.
- Added MIT `LICENSE`.
- Added `CHANGELOG.md` to track future skill changes.
- Added examples for `debugging` and `testing`.

### Changed

- Documented repository-level maintenance expectations in `README.md`.
- Reworded `README.md` to describe the collection as general AI coding-agent skills rather than Cursor-only skills.
- Added usage guidance for non-Cursor tools such as project rule files, CLI agents, and chat-based assistants.
- Renamed the Makefile install target variable to the generic `SKILLS_DIR` while keeping `CURSOR_SKILLS_DIR` compatible.
- Renamed the project presentation to Harness Skills (`harness-skills`).
- Added README badges for license, skill count, checks, AI agent usage, and the GitHub repository.
- Strengthened `ci-quality` and `project-bootstrap` to strongly recommend pre-commit hooks.
- Switched the README check badge to the GitHub Actions CI workflow.
