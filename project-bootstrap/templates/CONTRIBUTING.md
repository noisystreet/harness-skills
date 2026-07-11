# Contributing

Thanks for contributing to `<project-name>`.

## Setup

```bash
# Install dependencies and enable local hooks
<pre-commit install commands>
make check
make test
```

## Development Flow

1. Create a short-lived branch from `main`.
2. Make a focused change with tests when behavior changes.
3. Run the project quality entry points before opening a PR.
4. Open a PR with motivation, summary, and a short test plan.

## Commit And PR Expectations

- Prefer Conventional Commits if the repository uses them.
- Keep PRs reviewable; split large changes when possible.
- Update docs and changelog for user-visible behavior.
- Do not commit secrets, real credentials, or machine-specific paths.

## Security

Do not report vulnerabilities in public issues.
Follow `SECURITY.md` for private disclosure.
