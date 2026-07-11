# CI Quality References

## Guides

- [GitHub Actions documentation](https://docs.github.com/en/actions) - workflows, caching, OIDC, artifacts.
- [pre-commit](https://pre-commit.com/) - local fast gates.
- [Conventional Commits](https://www.conventionalcommits.org/) - commit-msg automation when adopted.
- [SLSA](https://slsa.dev/) - supply-chain integrity levels for release pipelines.
- Language audit tools: `cargo deny`, `npm audit`, `pip-audit`, OSV scanners.

## What To Learn

- One quality entry for humans, agents, and CI.
- Keep pre-commit fast; put slow suites in CI.
- Fail closed on format/lint/tests; open ignores need owners and expiry.

## Caveats

- Copying another org's matrix blindly creates brittle CI.
- Security scanners need triage process, not only red/green badges.
