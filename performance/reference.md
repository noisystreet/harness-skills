# Performance References

## Guides

- [Brendan Gregg performance materials](https://www.brendangregg.com/) - profiling mental models and tools.
- [perf](https://perf.wiki.kernel.org/) / platform profilers / language benchmark harnesses.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) - overload and amplification context.

## What To Learn

- Measure end-to-end before micro-optimizing.
- Record budgets, environments, and before/after numbers.
- Guard hot paths with stable benchmarks when feasible.

## Caveats

- Microbenchmarks lie without careful harness setup and production-like data shapes.
