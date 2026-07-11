# Secure Coding Examples

## Secret In Logs

Bad:

```text
logger.info("auth success token=%s", request.headers["Authorization"])
```

Better:

```text
logger.info("auth success user_id=%s request_id=%s", user.id, request_id)
```

Notes:

- Never log raw tokens, cookies, passwords, or connection strings.
- Prefer identifiers and outcomes over request bodies.

## Path Traversal

Bad:

```python
path = Path("/var/data") / user_filename
return path.read_bytes()
```

Better:

```python
base = Path("/var/data").resolve()
path = (base / user_filename).resolve()
if not path.is_relative_to(base):
    raise PermissionError("path escapes allowed directory")
return path.read_bytes()
```

## SQL Injection

Bad:

```sql
SELECT * FROM orders WHERE user_id = '{user_id}' ORDER BY {sort}
```

Better:

```text
Use a parameterized query for values.
Allowlist sort columns: created_at, amount, status.
Reject unknown sort inputs instead of interpolating them.
```

## Shell Injection

Bad:

```bash
os.system(f"convert {user_path} /tmp/out.png")
```

Better:

```python
subprocess.run(
    ["convert", str(user_path), "/tmp/out.png"],
    check=True,
    timeout=30,
)
```

## Broken Authorization

Bad:

```text
GET /documents/{id}
- Looks up document by id.
- Returns it if authenticated.
```

Better:

```text
GET /documents/{id}
- Authenticate caller.
- Load document by id AND owner/tenant scope.
- Return 404 for cross-tenant access to avoid resource existence leaks when that is the project policy.
```

## Unsafe Deserialization

Bad:

```python
obj = pickle.loads(upload_bytes)
```

Better:

```text
Accept a documented JSON schema.
Validate type, size, and required fields.
Reject pickle/yaml unsafe loaders for untrusted input.
```

## Dependency Risk

Bad:

```text
curl https://example.com/install.sh | bash
```

Better:

```text
Add a pinned dependency through the project package manager.
Record why the dependency is needed.
Run the project's audit/lock workflow before merge.
```
