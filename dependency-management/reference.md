# Dependency Management References

## Guides

- [OpenSSF Secure Supply Chain guides](https://bestpractices.coreinfrastructure.org/) / [OpenSSF](https://openssf.org/) materials.
- [OSV](https://osv.dev/) - vulnerability database and tooling ecosystem.
- [REUSE](https://reuse.software/) / SPDX - license hygiene.
- Ecosystem auditors: `cargo deny`, `npm audit`, `pip-audit`, Dependabot/Renovate docs.

## What To Learn

- Justify new dependencies; prefer stdlib and existing stack.
- Lock and review diffs; triage advisories with owners and expiry.
- Treat install scripts and build hooks as code execution.

## Caveats

- Zero CVEs is not always achievable; document risk acceptance explicitly.
