# Testing References

## Guides

- [ISTQB materials](https://www.istqb.org/) - shared vocabulary for test levels and techniques.
- [Martin Fowler: TestPyramid](https://martinfowler.com/bliki/TestPyramid.html) - balancing unit/integration/E2E cost.
- [xUnit Test Patterns](http://xunitpatterns.com/) - fixture and assertion smell catalog.
- pytest / cargo test / CTest docs for language-specific runners (see language `*-style` skills).

## Books

- `Working Effectively with Legacy Code` - characterization tests and seams.
- `Unit Testing Principles, Practices, and Patterns` - maintainable tests and anti-patterns.

## What To Learn

- Optimize for bug-finding value per minute, not line coverage vanity.
- Prefer deterministic tests; quarantine flakes with ownership.
- Lock behavior before refactors with characterization tests.

## Caveats

- Pyramid shape depends on the system; contracts and message systems may need more integration tests.
