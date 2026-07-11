# Migration Examples

## Expand / Contract Column

Bad:

```text
Rename users.name to users.display_name in one deploy,
update all writers, and drop the old column immediately.
```

Better:

```text
1. Add display_name (nullable).
2. Dual-write name and display_name.
3. Backfill display_name from name.
4. Switch readers to display_name.
5. Stop writing name after verification.
6. Drop name in a later release.
```

## Message Format Change

```text
Goal: add optional field "priority" to jobs.
Steps:
1. Consumers accept messages with or without priority (default normal).
2. Deploy consumers.
3. Producers start sending priority.
4. Metrics: parse errors stay flat; priority distribution looks sane.
```

## API Deprecation Window

```text
GET /v1/reports remains.
GET /v2/reports ships with clearer pagination.
Docs/CHANGELOG mark v1 deprecated with removal date.
Traffic dashboard shows v1 share before contract removal.
```

## Rollback Note

```text
Step switch_read_to_new_index:
- Forward: flip config read_index=new
- Rollback: flip read_index=old (no data rewrite needed)
- Do not drop old index until rollback window ends
```
