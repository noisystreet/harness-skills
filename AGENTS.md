# AGENTS.md

## Project Identity

- Project: personal Cursor Agent Skills collection
- Purpose: maintain reusable skills for common software engineering workflows
- Runtime: Markdown skills plus a small Python checker invoked by `make check`

## Directory Overview

```text
.
├── */SKILL.md                  # one skill per directory
├── */examples.md               # optional examples for high-frequency skills
├── */reference.md              # optional details for edge cases
├── */templates/                # optional reusable output templates
├── tools/check_skills.py       # repository validation
├── Makefile                    # install/list/check/uninstall
└── README.md                   # catalog and usage
```

## Required Commands

After changing skills, templates, examples, README, or validation logic:

```bash
make check
make install
```

Use `make list` to confirm global links.

## Skill Authoring Rules

- Prefer updating an existing skill before adding a new one.
- Keep each `SKILL.md` focused and under 500 lines.
- `name` must match the directory name.
- `description` must be specific and include trigger terms.
- Put bulky examples in `examples.md`; put edge cases in `reference.md`; put reusable forms in `templates/`.
- Do not duplicate detailed rules in `development-workflow`; it only routes to concrete skills.

## Documentation Rules

- Update `README.md` when adding, renaming, or removing a skill.
- Update `CHANGELOG.md` for user-visible changes to this collection.
- Keep commands in README aligned with `Makefile`.

## Security And Privacy

- Do not add real secrets, tokens, credentials, cookies, private keys, or internal URLs.
- Do not add user-specific absolute paths to user-facing docs or skills.
- Example credentials must be obvious placeholders.

## Git Workflow

- Default branch: `main`.
- Use Conventional Commit style where practical.
- Run `make check` before committing.
