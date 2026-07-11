# AGENTS.md

## Project Identity

- Project:
- Purpose:
- Tech stack:
- Target runtime/platform:

## Directory Overview

```text
.
├── src/
├── tests/
└── docs/
```

## Hard Constraints

- Module dependency direction:
- Forbidden dependencies:
- Architecture docs that require human approval before editing:
- Security red lines:
  - Do not commit secrets, tokens, certificates, cookies, or private keys.
  - Do not bypass authentication, authorization, or input validation.

## Required Commands

Run the project-specific equivalents:

```bash
make check
make test
```

## Coding Rules

- Follow the repository style first.
- Keep behavior changes covered by tests.
- Keep public API and serialized data compatibility explicit.

## Documentation Rules

- API changes update API docs.
- Architecture changes update architecture docs or ADRs.
- User-visible changes update CHANGELOG or release notes.
