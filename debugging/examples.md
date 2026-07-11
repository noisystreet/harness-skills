# Debugging Examples

## Failing Test

Input:

```text
`pytest tests/test_tokens.py::test_expired_refresh_token` fails with:
Expected Unauthorized, got OK.
```

Output:

```markdown
## Root cause
Refresh-token rotation runs before expiry validation, so an expired token can
receive a new access token.

## Evidence
- The failing test passes when expiry validation is moved before rotation.
- Logs show `rotate_token()` runs before `validate_expiry()`.

## Fix
- Validate token expiry before rotating credentials.
- Add a regression test for expired refresh tokens.

## Verification
- `uv run pytest tests/test_tokens.py::test_expired_refresh_token`
```

## Flaky Test

Input:

```text
CI intermittently fails `test_worker_drains_queue`; rerun usually passes.
```

Output:

```markdown
## Root cause
The test asserts queue length immediately after starting the worker. The worker
and assertion race each other, so timing determines the result.

## Evidence
- Failure disappears when waiting for the queue-empty condition.
- No production code changes are required to reproduce/fix the test.

## Fix
- Replace fixed timing assumptions with condition waiting and a timeout.
- Ensure each test uses an isolated queue.

## Verification
- `pytest tests/test_worker.py::test_worker_drains_queue -x`
- Repeated locally with the flaky seed / CI retry command
```

## Performance Regression

Input:

```text
Importing 10k records changed from ~2s to ~30s after validation refactor.
```

Output:

```markdown
## Root cause
Validation now performs a linear duplicate scan for every record, turning the
import path from O(n) into O(n^2).

## Evidence
- Profiling shows most time in `find_duplicate()`.
- Runtime grows quadratically as fixture size doubles.

## Fix
- Build a set of seen IDs once per batch.
- Keep validation behavior unchanged.

## Verification
- Existing import tests
- New large-batch regression test or benchmark
```

## Bad Debugging Pattern

Avoid:

```markdown
I changed the retry logic, increased sleeps, and swallowed the error.
```

Prefer:

```markdown
I reproduced the failure, identified the timeout as the first failing boundary,
changed only the timeout propagation, and added a regression test.
```
