# Development Workflow Examples

## Route A Feature Request

```text
User: implement rate limiting for the public API
Route:
1. api-design (error semantics, headers, compatibility)
2. data-modeling / runtime-reliability (limits, idempotency)
3. clean-code + language *-style
4. testing + secure-coding
5. docs-style (changelog / API notes)
6. commit-message + github-flow
```

## Route A Slow Endpoint

```text
User: checkout is slow in production
Route:
1. observability (confirm signals exist)
2. performance (budget, measure, profile)
3. debugging (if root cause unclear)
4. testing (regression / benchmark guard)
```

## Route An Unfamiliar Repo

```text
User: help me understand this codebase
Route:
1. codebase-analysis (briefing)
2. docs-style only if asked to write ARCHITECTURE/ADR
3. Do not jump to refactoring without a goal
```

## Anti-Pattern

Bad:

```text
Load every skill and rewrite the project layout first.
```

Better:

```text
Pick the smallest route for the task.
Defer architecture/refactor skills until the user asks for structural change.
```
