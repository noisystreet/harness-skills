# API Design References

## Guides

- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines) - pragmatic HTTP API conventions.
- [Google AIP](https://google.aip.dev/) - resource-oriented API design patterns.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) - contract documentation format.
- [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/) - evolution and compatibility practices.

## What To Learn

- Treat error codes, pagination, and idempotency as part of the public contract.
- Prefer additive evolution; document deprecations with dates.
- Keep DTO contracts separate from internal persistence models.

## Caveats

- Guidelines differ; follow the repository's existing public API style first.
