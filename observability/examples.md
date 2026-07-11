# Observability Examples

## Structured Log Event

Bad:

```text
log("db failed again!!!")
```

Better:

```json
{
  "level": "error",
  "msg": "database query failed",
  "request_id": "req_123",
  "op": "list_orders",
  "db.statement": "select_orders_by_user",
  "error.kind": "timeout",
  "latency_ms": 3004
}
```

## High-Cardinality Metrics

Bad:

```text
http_requests_total{user_id="42", email="a@example.com"}
```

Better:

```text
http_requests_total{route="/orders", method="GET", status_class="2xx"}
```

Keep user identity in logs/traces when needed, not as metric labels.

## Alert That Helps

Bad:

```text
Alert when log line contains "error"
```

Better:

```text
Alert when 5m success-rate SLO burn is high for checkout.
Page includes:
- current burn rate and window
- affected region
- dashboard link
- first checks: dependency errors, deploy marker, queue lag
```

## Correlation Across Queue

Bad:

```text
HTTP handler logs request_id.
Worker logs only job payload fields.
No shared id between produce and consume.
```

Better:

```text
Producer puts trace_id/request_id into message metadata.
Consumer continues the same trace and logs the same ids.
Dead-letter entries retain the ids for replay investigation.
```
