# Code Review Examples

## Finding With Clear Impact

```markdown
## Findings
- [High] `src/auth/session.py`: expired refresh tokens are rotated before expiry
  is checked. A stale session can receive a new access token, extending access
  beyond the intended lifetime. Check expiry before rotation and add a regression
  test for expired refresh tokens.

## Summary
The implementation is close, but token expiry order is a blocking auth bug.
```

## Test Gap

```markdown
## Findings
- [Medium] `src/imports/parser.rs`: the new duplicate-record branch has no
  regression test. This is a user-visible error path and easy to break during
  parser refactors. Add a test covering duplicate IDs in one input batch.

## Summary
No correctness issue found in the main path; residual risk is the untested
duplicate-record branch.
```

## Security Concern

```markdown
## Findings
- [Critical] `src/routes/files.ts`: the download path is built directly from
  `req.query.name`. A value like `../../.env` can escape the intended directory.
  Normalize the path and verify it remains under the allowed root before reading.

## Summary
The file endpoint needs a path traversal fix before merge.
```

## Non-Blocking Nit

```markdown
## Findings
- [Low] `src/cli/main.rs`: nit: `run_import` now validates and executes the
  import. Splitting validation into a helper would make the dry-run path easier
  to follow, but this should not block the PR.

## Summary
No blocking issues found. Tests cover the new dry-run behavior.
```

## No Findings

```markdown
未发现阻塞问题。

测试覆盖了新增行为和主要错误路径。剩余风险是未在真实外部服务上做端到端验证；当前 mock 覆盖了请求/响应契约。
```

## Bad Review Patterns

Avoid:

```markdown
Looks good.
```

Avoid:

```markdown
很多地方风格不太好，建议整体重构。
```

Prefer:

```markdown
## Findings
- [Medium] `src/config.py`: `load_config()` reads environment variables from
  three different branches, so precedence depends on which branch runs first.
  Centralize precedence as CLI args -> env -> file -> defaults to match the
  documented config model.
```
