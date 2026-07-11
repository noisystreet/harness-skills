# Performance Examples

## Measurement First

Bad:

```text
Rewrite the serializer in a faster language because the API feels slow.
```

Better:

```text
1. Budget: checkout p95 < 300ms under 50 RPS.
2. Trace shows 220ms in inventory HTTP call, 20ms local work.
3. Fix inventory timeout/pooling first; leave serializer alone.
4. Re-measure p95 after the change.
```

## N+1 Query

Bad:

```text
for order in orders:
    items = db.query("select * from items where order_id=?", order.id)
```

Better:

```text
Load orders once.
Load items for all order ids in one query (or a documented join).
Benchmark list endpoint before/after with the same fixture size.
```

## Cache Without Bounds

Bad:

```text
cache[key] = expensive()  # never evicts
```

Better:

```text
Use an LRU/TTL cache with max entries and explicit invalidation.
Add metrics for hit rate, size, and eviction.
Document stampede behavior under miss storms.
```

## Benchmark Guard

```text
bench_name: parse_manifest_10k
command: cargo bench parse_manifest_10k / pytest --benchmark ...
budget: p95 < 25ms on CI medium runner
fail if median regresses > 15% versus main baseline
```
