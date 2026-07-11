# Project Bootstrap Examples

## Minimal New Python Service

```text
1. uv init + src layout + pytest
2. README with run/test commands
3. AGENTS.md with hard constraints
4. .env.example + SECURITY.md
5. .pre-commit-config.yaml
6. GitHub Actions calling make check / make test
```

## Do Not Over-Scaffold

Bad:

```text
Add Kubernetes, service mesh, and multi-region templates
for a weekend CLI tool.
```

Better:

```text
Ship README, tests, lint/format, and a single build entry first.
Add deploy topology when there is a real deployment target.
```

## Agent Entry Doc

```markdown
# AGENTS.md
- Stack: Rust 2024, axum
- Do not add ORM X
- Always run: cargo fmt && cargo clippy -D warnings && cargo nextest run
- Never commit secrets
```
