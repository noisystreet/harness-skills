# AGENTS.md

## Project Identity

- Project: Harness Skills (`harness-skills`)
- Purpose: maintain reusable skills and workflow rules for harnessing AI coding agents in software engineering projects
- Runtime: Markdown skills plus a small Python checker invoked by `make check`

## Directory Overview

```text
.
├── */SKILL.md                  # one skill per directory
├── */examples.md               # optional examples for high-frequency skills
├── */reference.md              # optional details for edge cases
├── */templates/                # optional reusable output templates
├── tools/check_skills.py       # repository validation
├── tools/catalog_skills.py     # README catalog generation
├── tools/cut_changelog.py      # changelog cutover / release notes extract
├── tools/release_flow.py       # protected-main release PR/tag helpers
├── Makefile                    # install/list/check/catalog/release-pr/release-tag
└── README.md                   # catalog and usage
```

## Required Commands

After changing skills, templates, examples, README, or validation logic:

```bash
make catalog
make check
make install
```

Use `make list` to confirm global links.

To cut a release when `main` is PR-protected:

```bash
make release-pr VERSION=x.y.z
# after merge:
make release-tag VERSION=x.y.z PUSH=1
```

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
