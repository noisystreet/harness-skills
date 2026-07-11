# Dependency Management Examples

## Adding A Dependency

Bad:

```text
Add a full web framework to format timestamps.
```

Better:

```text
Need RFC3339 formatting in one service.
Prefer stdlib or already-present time utilities.
If a crate/lib is required, document why and the rejected alternatives.
```

## Lockfile Change In PR

Bad:

```text
PR title: chore: update deps
Diff: 2,000 lockfile lines, no explanation
```

Better:

```text
PR summary:
- Upgrade serde 1.0.210 -> 1.0.219 for advisory XYZ
- No intentional public API changes
- Ran: cargo deny check && cargo nextest run
```

## Ignoring An Advisory

Bad:

```text
exclude advisory forever because CI is red
```

Better:

```text
Temporary ignore with:
- advisory id
- affected package
- why we are not reachable / not exploitable
- expiry or follow-up issue for upgrade
```

## Removing Dead Weight

```text
Observed: unused HTTP client left after refactor.
Actions:
1. remove direct dependency
2. refresh lockfile
3. grep for imports and docs
4. run tests and package/build
```
