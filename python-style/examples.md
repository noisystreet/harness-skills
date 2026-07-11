# Python Style Examples

## Typed Public API

Bad:

```python
def load_user(user_id):
    return db.find(user_id)
```

Better:

```python
def load_user(user_id: str) -> User | None:
    return db.find(user_id)
```

## No Mutable Default

Bad:

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket
```

Better:

```python
def add_item(item: Item, bucket: list[Item] | None = None) -> list[Item]:
    data = bucket if bucket is not None else []
    data.append(item)
    return data
```

## Narrow Exception Handling

Bad:

```python
try:
    process(msg)
except Exception:
    pass
```

Better:

```python
try:
    process(msg)
except ValidationError as exc:
    logger.warning("invalid message", extra={"error": str(exc)})
    raise
```
