# Debugging References

## Guides

- [Andreas Zeller: Why Programs Fail](https://www.whyprogramsfail.com/) - systematic debugging concepts.
- [RR / time-travel debugging resources](https://rr-project.org/) - for hard reproducibility cases on supported platforms.
- Language tooling: sanitizers, `gdb`/`lldb`, pytest failure bisects, cargo/nextest filters.

## What To Learn

- Reproduce first; change one variable per experiment.
- Prefer evidence from tests, logs, and bisect over intuition alone.
- Fix root causes; leave a regression test behind.

## Caveats

- Production-only failures need observability and safe experimentation, not local guess loops.
