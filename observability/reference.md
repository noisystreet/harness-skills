# Observability References

## Guides

- [OpenTelemetry docs](https://opentelemetry.io/docs/) - traces, metrics, logs correlation.
- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) - actionable monitoring.
- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) - burn-rate alerting.
- RED / USE method writeups for service and resource metrics.

## What To Learn

- Correlate with stable IDs across logs, metrics, and traces.
- Alert on user impact / SLO burn, not every error line.
- Control metric cardinality from day one.

## Caveats

- Vendor dashboards are not a substitute for clear SLIs.
- Sampling and retention policies are production constraints, not afterthoughts.
