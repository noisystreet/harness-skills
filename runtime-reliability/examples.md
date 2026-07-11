# Runtime Reliability Examples

## Health Checks

Bad:

```text
GET /health always returns 200 if the process is running.
```

Better:

```text
GET /live
- Returns 200 when the process event loop is alive.
- Does not depend on database availability.

GET /ready
- Returns 200 only when config is loaded, database pool is ready, and the
  worker queue can accept work.
- Returns 503 during startup, draining, or dependency outage.
```

## Graceful Shutdown

Scenario:

```text
Worker receives SIGTERM while processing jobs.
```

Expected behavior:

1. Stop polling new jobs.
2. Mark readiness false.
3. Let in-flight jobs finish within a timeout.
4. Nack or release unfinished jobs.
5. Flush logs/metrics and close connections.
6. Exit non-zero only if shutdown could not complete safely.

## Retry Policy

Bad:

```text
Retry forever every 100 ms.
```

Better:

```text
Retry at most 5 times with exponential backoff and jitter.
Retry only on timeouts and 5xx responses.
Do not retry validation errors, auth errors, or non-idempotent operations
without an idempotency key.
```

## Backpressure

Scenario:

```text
HTTP endpoint enqueues import jobs.
```

Good behavior:

- Queue has a maximum size.
- When full, return `429` or `503` with retry guidance.
- Metrics expose queue depth and rejection count.
- Logs include request_id and job type, not sensitive payloads.

## Poison Message

Bad:

```text
One malformed message is retried forever and blocks the queue.
```

Better:

```text
After a bounded number of attempts, move the message to a dead-letter queue,
record the reason, and continue processing other messages.
```
