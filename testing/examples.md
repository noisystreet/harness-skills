# Testing Examples

## Bug Regression Test

Scenario:

```text
Expired refresh tokens were accepted because rotation happened before expiry validation.
```

Good test intent:

```text
Given an expired refresh token
When the refresh endpoint is called
Then the request is rejected and no new token is issued
```

Test plan entry:

```markdown
- [x] Added regression test for expired refresh token rejection
- [x] Ran focused auth tests
```

## Parameterized Edge Cases

Scenario:

```text
Import parser validates record IDs.
```

Good cases:

```text
- empty ID -> invalid
- whitespace ID -> invalid
- duplicate ID in same batch -> invalid
- valid unique IDs -> accepted
```

Avoid one large test that mixes all failures. Prefer parameterized cases with
clear expected errors.

## Flaky Test Fix

Bad:

```text
sleep(5)
assert queue.empty()
```

Good:

```text
wait_until(lambda: queue.empty(), timeout=5)
assert processed_count == expected_count
```

Why:

```text
The test waits for a condition with a bounded timeout instead of assuming a
specific machine speed.
```

## Mock Boundary

Bad:

```text
Mock every internal function, then assert the mocks were called.
```

Good:

```text
Mock the external payment provider; assert the service records a successful
payment and returns the expected response.
```

## Test Plan

```markdown
## Test plan
- [x] Unit tests for validation edge cases
- [x] Integration test for duplicate records in one batch
- [x] Regression test for the reported bug
- [ ] Manual check of external provider sandbox (not available locally)
```

## Bad Testing Pattern

Avoid:

```text
Added a test that imports the module and asserts True.
```

Prefer:

```text
Added a test that fails on the old behavior and passes only when the user-visible
bug is fixed.
```
