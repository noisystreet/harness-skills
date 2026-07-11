# Clean Code Examples

## Flag Soup → Explicit State

Bad:

```text
started=false, done=false, failed=false
```

Better:

```text
enum Phase { Ready, Running, Done, Failed }
```

## Hidden Member Dependency

Bad:

```text
obj.cache = load()
obj.process()  # callers cannot see the dependency
```

Better:

```text
data = load()
obj.process(data)
```

## Query With Side Effects

Bad:

```text
count = registry.get_count()  # also flushes and clears flags
```

Better:

```text
registry.flush()
count = registry.count()
```

## Pattern Only When Needed

Bad:

```text
Introduce Strategy + AbstractFactory for two almost identical formatters.
```

Better:

```text
Start with a function or enum match.
Extract a strategy only after a third variant appears or branching hurts tests.
```
