# Docs Style Examples

## README That Can Be Executed

Bad:

```markdown
# Project
A next-generation platform for synergy.
```

Better:

```markdown
# Project
CLI that converts manifests to deploy specs.

## Run
make check
make test
./target/release/project convert examples/app.yaml
```

## ADR With Real Trade-Off

Bad:

```markdown
## Decision
Use Postgres.
```

Better:

```markdown
## Decision
Use Postgres 16 with JSONB for flexible attributes.

## Consequences
+ Strong transactions and operational familiarity
- JSONB queries need indexed paths; avoid unbounded documents
- Team must own backup/migration discipline

## Alternatives Considered
SQLite: too weak for multi-writer service
DynamoDB: stronger ops burden for current team size
```

## Changelog Entry

Bad:

```markdown
### Changed
- misc fixes
```

Better:

```markdown
### Changed
- Audit export now uses cursor pagination; `offset` is deprecated.

### Migration
- Clients should switch to `cursor` before 2026-10-01.
```
