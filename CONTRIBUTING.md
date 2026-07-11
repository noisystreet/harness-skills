# Contributing

Harness Skills is a Markdown-based collection of reusable AI coding-agent skills.
Contributions should keep the collection focused, portable, and easy to validate.

## Before Adding A Skill

Prefer updating an existing skill unless the new topic has a distinct trigger,
audience, and workflow.

Good reasons to add a skill:

- A new task type needs its own routing or output format.
- Existing skills would become too broad if the content were added there.
- The skill has clear trigger terms and reusable rules.

## Skill Structure

Each skill lives in its own directory:

```text
skill-name/
├── SKILL.md
├── examples.md      # optional
├── reference.md     # optional
└── templates/       # optional
```

Rules:

- Directory names use `kebab-case`.
- `SKILL.md` frontmatter `name` must match the directory name.
- `description` must explain what the skill does and when to use it.
- Keep `SKILL.md` under 500 lines.
- Put bulky examples in `examples.md`.
- Put edge cases in `reference.md`.
- Put reusable output forms in `templates/`.

## Documentation

When adding, renaming, or removing a skill:

1. Update `README.md`.
2. Update `CHANGELOG.md`.
3. Add examples/templates only when they improve output quality.

Do not add real secrets, internal URLs, user-specific absolute paths, or private
project details.

## Local Checks

Install hooks:

```bash
pre-commit install
pre-commit run --all-files
```

Run repository checks:

```bash
make check
make install
make list
```

`make check` validates skill metadata, README links, file references, empty
templates/examples, and user-specific absolute paths.

## Releases

1. Record user-visible changes under `CHANGELOG.md` `[Unreleased]`.
2. On `main` after merge:
   ```bash
   make release VERSION=x.y.z
   git push origin HEAD
   git push origin vx.y.z
   ```
3. Pushing the `v*` tag creates a GitHub Release whose body is extracted from
   that CHANGELOG section.

## Commit Messages

Use clear Conventional Commit style where practical:

```text
feat(skill): add api design examples
docs(readme): document external agent usage
chore(ci): add pre-commit checks
```

## Pull Requests

PRs should include:

- Summary of changed skills or docs
- Test plan (`make check`, `pre-commit run --all-files`, or why not run)
- Any compatibility impact for existing skill users
