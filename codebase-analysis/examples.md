# Codebase Analysis Examples

## Library Onboarding

Bad:

```text
Open random utility files and summarize coding style only.
```

Better:

```text
1. Read README + crate/package docs for intended use.
2. Locate public API surface (lib.rs / __init__.py / include headers).
3. Trace one example from docs through implementation.
4. Briefing: purpose, public API, extension points, uncertainties.
```

## Service Map

Scenario:

```text
Unfamiliar HTTP service repo. Need to know how a request becomes a DB write.
```

Output sketch:

```markdown
### Entrypoints
- cmd/server/main.go registers /v1/orders

### Primary Flow
1. Handler ParseCreateOrder
2. Service CreateOrder (domain invariants)
3. Repo InsertOrder
4. Outbox publish OrderCreated

### Uncertainties
- Whether outbox dispatcher is in-process or separate worker (no README mention)
```

## Verify With A Command

```text
Claim: "make test runs unit tests only"
Check: open Makefile / CI, run make test if safe
Result: also runs integration tests requiring Docker → update briefing
```

## Stop Conditions

```text
User asked: map auth module only.
Do: entrypoints, token validation flow, session store boundary.
Don't: rewrite auth, expand into billing, or drive-by renames.
```
