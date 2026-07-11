# API Design Examples

## Cursor Pagination

Scenario:

```text
List audit events for an organization. The table can grow large and new events
arrive while clients are paging.
```

Good shape:

```http
GET /orgs/{org_id}/audit-events?limit=50&cursor=eyJ...
```

```json
{
  "items": [
    {
      "id": "evt_123",
      "type": "user.invited",
      "created_at": "2026-07-11T12:00:00Z"
    }
  ],
  "next_cursor": "eyJ...",
  "has_more": true
}
```

Notes:

- `limit` has a documented default and maximum.
- Sort order is stable.
- Cursor format is opaque to clients.

## Field Validation Error

```http
POST /imports
```

```json
{
  "source": "",
  "mode": "unknown"
}
```

```json
{
  "error": {
    "code": "invalid_request",
    "message": "The request contains invalid fields.",
    "details": [
      {
        "field": "source",
        "code": "required",
        "message": "source is required"
      },
      {
        "field": "mode",
        "code": "unsupported_value",
        "message": "mode must be one of: preview, apply"
      }
    ],
    "request_id": "req_123"
  }
}
```

Avoid returning only:

```json
{ "error": "bad request" }
```

## Idempotent Create

Scenario:

```text
Client creates a payment and may retry after a timeout.
```

Good requirements:

- Client sends `Idempotency-Key`.
- Server stores the first successful result for a documented window.
- Retrying with the same key and same payload returns the same result.
- Retrying with the same key and different payload returns a conflict.

```http
POST /payments
Idempotency-Key: 3f7c...
```

## Breaking Change

Bad:

```text
Rename response field `user_id` to `actor_id` in place.
```

Good:

```text
Add `actor_id` while keeping `user_id` deprecated for one version.
Document migration steps and add a CHANGELOG entry.
Remove `user_id` only in the next breaking version.
```
