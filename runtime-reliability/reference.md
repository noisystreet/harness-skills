# Runtime Reliability References

## Guides

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) - overload, rollback, and operational principles.
- [AWS / Azure / GCP reliability pillars docs](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) - cloud reliability checklists (adapt, do not copy blindly).
- Queue/worker docs for the project's broker (ack/nack, visibility timeout, DLQ).
- Pair with `observability` references for signals and `release` for rollback.

## What To Learn

- Timeouts, retries, backoff, and idempotency are default design, not polish.
- Separate liveness from readiness.
- Feature flags need owners and cleanup dates.

## Caveats

- Cloud vendor guidance embeds their service assumptions; translate to your runtime.
