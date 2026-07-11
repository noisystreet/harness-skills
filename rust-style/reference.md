# Rust Style References

Use these references as calibration points when applying `rust-style`. Prefer the current repository's established conventions when they conflict with a general reference.

## Official Guides

- [The Rust Programming Language](https://doc.rust-lang.org/book/) - language fundamentals, ownership, borrowing, enums, traits, and error handling.
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) - naming, trait design, conversions, errors, documentation, and compatibility for public APIs.
- [Rust Reference](https://doc.rust-lang.org/reference/) - precise language semantics when style decisions depend on compiler behavior.
- [The Rustonomicon](https://doc.rust-lang.org/nomicon/) - unsafe Rust, aliasing, lifetimes, variance, and memory model topics.
- [Clippy Lints](https://rust-lang.github.io/rust-clippy/) - idiom and correctness checks that often encode community norms.
- [Rustfmt](https://rust-lang.github.io/rustfmt/) - formatting behavior and configuration.

## Books And Courses

- `Programming Rust` - strong practical coverage of ownership, traits, concurrency, and systems code.
- `Rust for Rustaceans` - advanced idioms, API design, async, unsafe, and crate architecture.
- `Zero To Production In Rust` - service-oriented Rust, error handling, testing, telemetry, and deployment.
- `Command-Line Rust` - practical CLI structure, tests, and error handling patterns.

## Exemplary Projects

- [ripgrep](https://github.com/BurntSushi/ripgrep) - CLI ergonomics, error handling, performance-conscious structure, and testing.
- [serde](https://github.com/serde-rs/serde) - public API design, traits, feature flags, documentation, and compatibility discipline.
- [tokio](https://github.com/tokio-rs/tokio) - async runtime design, module boundaries, docs, and production-grade testing.
- [cargo](https://github.com/rust-lang/cargo) - large Rust application architecture, diagnostics, workflows, and compatibility.
- [rust-analyzer](https://github.com/rust-lang/rust-analyzer) - large codebase organization, incremental computation, and clear internal APIs.

## What To Learn

- Model mutually exclusive state with enums and typed transitions rather than boolean flag combinations.
- Keep public APIs narrow, documented, and compatible; use feature flags intentionally.
- Preserve error context at boundaries while keeping library error types stable and typed.
- Prefer small `unsafe` blocks with explicit invariants and safe wrappers around them.
- Treat tooling (`fmt`, `clippy`, `nextest`, dependency checks) as part of the style baseline.

## Caveats

- Large projects carry historical constraints; do not copy their internal patterns without understanding why they exist.
- `unsafe`, macros, and advanced trait tricks require stronger justification than ordinary code.
- Framework-heavy examples may optimize for extensibility or performance beyond a small project's needs.
