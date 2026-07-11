# Refactoring Examples

## Extract Without Behavior Change

Bad:

```text
Rewrite the billing module and fix three bugs in the same PR.
```

Better:

```text
PR 1: extract invoice totals helper; same public results; tests green.
PR 2: fix rounding bug with a new regression test.
```

## Characterization Before Touching Legacy

```text
Legacy: fee calculator with undocumented edge cases.
Steps:
1. Capture fixtures for common plans and odd remainders.
2. Assert current outputs byte-for-byte / decimal-for-decimal.
3. Extract pure function behind the same API.
4. Keep fixtures green throughout.
```

## Strangler Path

```text
Goal: replace XML config loader with JSON loader.
Steps:
1. Add JSON loader behind a feature flag / adapter interface.
2. Dual-run in tests: XML and JSON produce equivalent domain model.
3. Switch callers gradually.
4. Remove XML path and docs in a final cleanup PR.
```

## Rename Across Boundary

Bad:

```text
Rename User to Account across service, DB, API, and mobile client in one commit.
```

Better:

```text
1. Internal rename behind stable API field names.
2. Add API alias / migration notes if external name must change.
3. Coordinate consumers separately with compatibility window.
```
