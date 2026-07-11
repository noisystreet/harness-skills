# Migration References

## Guides

- expand/contract migration writeups (search "parallel change" / "expand contract pattern").
- [Martin Fowler: Parallel Change](https://martinfowler.com/bliki/ParallelChange.html)
- Database vendor online DDL docs for the project's engine.
- Pair with `api-design` compatibility rules and `release` rollback planning.

## What To Learn

- Design for coexistence of old and new readers/writers.
- Backfills must be resumable and observable.
- Destructive contract steps need an explicit no-rollback warning.

## Caveats

- Data shape and traffic volume dominate theory; always estimate lock/backfill cost.
