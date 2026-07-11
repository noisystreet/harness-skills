# Commit Message Examples

## Bug fix

Input:

```text
Auth refresh endpoint now checks token expiry before rotating credentials.
Added regression test for expired refresh tokens.
```

Output:

```text
fix(auth): reject expired refresh tokens

Validate token expiry before rotating credentials so stale sessions cannot
receive a new access token.
```

## Feature

Input:

```text
CLI import command supports --dry-run and prints the planned changes without
writing to disk.
```

Output:

```text
feat(cli): add dry-run mode for imports

Allow users to preview import changes before mutating local files.
```

## Refactor

Input:

```text
Parser no longer tracks started/done/failed booleans separately. It now uses a
single ParseState enum. No external behavior changed.
```

Output:

```text
refactor(parser): replace boolean flags with parse state
```

## Tests only

Input:

```text
Added table-driven tests for empty input, invalid IDs, and duplicate records.
No production code changed.
```

Output:

```text
test(imports): cover invalid record inputs
```

## CI / tooling

Input:

```text
GitHub Actions now runs ruff format, ruff check, pytest, and pyright for Python
pull requests.
```

Output:

```text
ci(python): add quality checks for pull requests
```

## Split needed

Input:

```text
Adds login endpoint, rewrites parser state handling, updates README, and bumps
several dependencies.
```

Output:

```text
建议拆提交：
1. feat(auth): add login endpoint
2. refactor(parser): replace boolean flags with parse state
3. docs(readme): update setup instructions
4. chore(deps): update dependencies
```

## Bad examples

Avoid:

```text
update files
fix bug
wip
misc changes
```

Prefer:

```text
fix(api): handle missing tenant id
docs(readme): document uv setup
chore(deps): update lint dependencies
```
