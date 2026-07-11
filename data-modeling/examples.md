# Data Modeling Examples

## Invariant In The Model

Bad:

```text
order.total can be negative; UI usually prevents it.
```

Better:

```text
Money/total construction rejects negative values.
Persistence constraint checks non-negative amounts.
Tests cover reject path for negative totals.
```

## Aggregate Boundary

Bad:

```text
Update Order, Inventory, and CustomerCredit in one shared mutable graph
across three services inside one request without failure handling.
```

Better:

```text
Order aggregate commits locally.
Emit OrderPlaced.
Inventory and credit handlers are idempotent consumers with retries/compensation.
Document eventual consistency window.
```

## Idempotency Key

```text
CreatePayment(request_id=req_123, invoice_id=inv_9, amount=10.00)
First call: pays once and stores result under (tenant, request_id).
Retry with same key: returns same result, no second capture.
Different amount same key: rejected as conflict.
```

## Soft Delete Uniqueness

Bad:

```text
unique(email) while deleted rows keep emails, blocking re-registration.
```

Better:

```text
unique(email) where deleted_at is null
or unique(email, deleted_at) with explicit tombstone strategy.
Document restore behavior.
```
