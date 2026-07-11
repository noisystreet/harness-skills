# Clean Code References

Use these references as background for `clean-code`. They are not a single rulebook; apply them through the language-specific skills and the current repository's conventions.

## Books And Essays

- `A Philosophy of Software Design` - complexity, deep modules, information hiding, comments, and tactical vs strategic programming.
- `Refactoring` - safe behavior-preserving change, code smells, and stepwise restructuring.
- `Working Effectively with Legacy Code` - characterization tests, seams, and safe changes in difficult codebases.
- `Clean Code` - naming, function shape, comments, and readability heuristics; apply selectively with modern language idioms.
- `The Pragmatic Programmer` - practical engineering habits, coupling, automation, and ownership.
- `Domain-Driven Design` - ubiquitous language, boundaries, aggregates, and domain modeling for complex business systems.

## Useful Online References

- [Martin Fowler: Refactoring](https://refactoring.com/) - catalog and discussion of common refactorings.
- [Martin Fowler: Bliki](https://martinfowler.com/bliki/) - short essays on architecture, design, and refactoring trade-offs.
- [Google Engineering Practices](https://google.github.io/eng-practices/) - code review, readability, and maintainability practices.
- [Architecture Decision Records](https://adr.github.io/) - lightweight architectural decision documentation.

## Exemplary Project Traits

Look for these traits in mature open-source projects rather than copying one project's style wholesale:

- Clear module boundaries and a small public surface.
- Explicit state transitions instead of scattered mutable flags.
- Tests that describe behavior and regressions, not incidental implementation.
- Errors that preserve context and are handled at meaningful boundaries.
- Documentation that explains constraints, invariants, and operational assumptions.

## What To Learn

- Reduce implicit state: make ownership, dependencies, phase, and side effects visible at the call site.
- Prefer names that encode domain intent over names that only describe data shape.
- Split code by responsibility and abstraction level, not by arbitrary "utils" buckets.
- Refactor in small verified steps; avoid broad cosmetic rewrites inside behavior changes.
- Use comments for intent, invariants, and surprising constraints, not for restating syntax.

## Caveats

- Classic books predate many modern language features; translate their intent into the target language's idioms.
- "Clean" is not a license for churn. Avoid renaming and restructuring that do not reduce real complexity.
- Large systems may need duplication, denormalization, or specialized data paths for performance; document those trade-offs instead of hiding them.
