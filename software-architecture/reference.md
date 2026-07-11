# Software Architecture References

Use these as calibration points. Prefer the repository's documented architecture when it conflicts with a general reference.

## Books

- `Software Architecture: The Hard Parts` - trade-offs, distributed systems decisions.
- `Fundamentals of Software Architecture` - characteristics, styles, soft skills of architecture.
- `Designing Data-Intensive Applications` - storage, consistency, derived data, batch/stream.
- `Domain-Driven Design` / `Implementing Domain-Driven Design` - bounded contexts and tactical modeling (pair with `data-modeling`).
- `Building Evolutionary Architectures` - fitness functions and incremental change.
- `A Philosophy of Software Design` - deep modules and complexity (also in `clean-code` references).

## Online

- [Architecture Decision Records](https://adr.github.io/) - lightweight decision records.
- [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar) - evolving technique awareness, not mandates.
- [C4 Model](https://c4model.com/) - context/container/component diagrams for communication.

## What To Learn

- Make quality attributes and constraints explicit before choosing a style.
- Keep dependency direction enforceable, not aspirational.
- Prefer evolutionary paths (modular monolith → extract) over big-bang rewrites.
- Record irreversible choices as ADRs.

## Caveats

- Case studies embed organizational constraints you may not share.
- Patterns and styles age; re-check applicability rather than copying diagrams.
