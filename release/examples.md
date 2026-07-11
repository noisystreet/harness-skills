# Release Examples

## Changelog Cutover

Bad:

```text
Tag v1.2.0 while CHANGELOG still only has [Unreleased].
```

Better:

```markdown
## [Unreleased]

## [1.2.0] - 2026-07-11

### Added
- Cursor pagination for audit events.

### Fixed
- Retry storm on upstream timeout.
```

## Canary Rollout

```text
1. Deploy v1.2.0 to 5% traffic.
2. Watch 15 minutes:
   - checkout success rate
   - p95 latency
   - error logs with release version
3. If budgets hold, 25% -> 100%.
4. If success rate drops beyond threshold, roll back to previous version.
```

## Rollback Matrix

| Change | Rollback |
|--------|----------|
| App binary/image only | Redeploy previous image/tag |
| Feature flag default on | Flip flag off |
| Expand-only DB column | Keep column; roll back app |
| Destructive contract drop | Usually NOT safely rollbackable; avoid bundling with first cutover |
```

## GitHub Release Notes

```text
Title: v0.1.0
Body:
- Summary of user-visible changes from CHANGELOG
- Upgrade/migration notes
- Verification commands
- Known limitations
```
