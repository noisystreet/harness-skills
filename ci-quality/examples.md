# CI Quality Examples

## Unified Local And CI Entry

Bad:

```text
README says: pytest
Developer runs: uv run pytest
CI runs: python -m pytest with different extras and no lint
```

Better:

```bash
# Makefile / justfile
make check   # format check + lint + type-check
make test    # unit tests

# CI
make check
make test
```

Notes:

- CI should call the same entry points people and agents use locally.
- Format jobs should check, not rewrite, in CI.

## Pre-commit Split

Good local hooks:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: detect-private-key

  - repo: local
    hooks:
      - id: lint
        name: lint
        entry: make lint
        language: system
        pass_filenames: false
```

Keep out of pre-commit:

```text
Full E2E suite
Nightly dependency audit against live advisories
Coverage upload and HTML report generation
```

## Incremental Coverage Gate

Bad:

```text
Fail every PR until whole-repo coverage jumps from 42% to 90%.
```

Better:

```text
Keep a realistic absolute floor if one exists.
Prefer patch/diff coverage gates for new and changed lines.
Raise the absolute floor gradually as debt is paid down.
```

## GitHub Actions Baseline

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Quality gates
        run: |
          make check
          make test
```

Optional slower jobs:

```text
schedule or main-only:
- dependency audit
- full E2E
- coverage upload
```

## Skipping Failures

Bad:

```yaml
continue-on-error: true  # because flaky
```

Better:

```text
Quarantine the flaky test with an issue link.
Fix ownership, timing, or isolation.
Keep the quality gate red until the suite is trustworthy again.
```
