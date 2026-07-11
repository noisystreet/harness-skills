# Software Architecture Examples

## Quality Attributes First

Bad:

```text
Adopt microservices because they are modern.
```

Better:

```text
Priority: independent deploy of billing + fault isolation from catalog.
Constraint: 6 engineers, weak distributed tracing today.
Decision: modular monolith with billing module boundary now;
revisit extract-service when deploy contention is proven.
ADR recorded.
```

## Dependency Rule

Bad:

```text
Domain OrderService imports Postgres repository and HTTP client directly.
```

Better:

```text
Domain depends on OrderRepository port.
Postgres adapter implements the port in infrastructure.
ARCHITECTURE.md states: domain -> ports; infra -> domain/ports (not reverse).
```

## Style Mismatch

Bad:

```text
Event-driven choreography for checkout that must be strongly consistent
atomic across payment + inventory, with no compensation model.
```

Better:

```text
Keep checkout as a synchronous application service / workflow with
explicit compensation, or document eventual consistency and customer UX.
```
