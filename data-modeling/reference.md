# Data Modeling References

## Books And Guides

- `Domain-Driven Design` / `Implementing Domain-Driven Design` - bounded contexts and tactical patterns.
- `Designing Data-Intensive Applications` - consistency, derived data, and storage trade-offs.
- [MariaDB/Postgres docs on constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) - enforce invariants in the database where appropriate.

## What To Learn

- Make invariants explicit in types, validation, and persistence constraints.
- Choose consistency boundaries deliberately; do not fake distributed ACID.
- Separate identity, attributes, and lifecycle state.

## Caveats

- DDD tactical patterns are optional machinery; use only when they reduce real complexity.
