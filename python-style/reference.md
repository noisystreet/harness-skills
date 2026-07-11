# Python Style References

Use these references as calibration points when applying `python-style`. Follow the target repository's established conventions first, especially for packaging, type checking, and test commands.

## Official Guides

- [PEP 8](https://peps.python.org/pep-0008/) - baseline Python style and naming guidance.
- [PEP 257](https://peps.python.org/pep-0257/) - docstring conventions.
- [PEP 484](https://peps.python.org/pep-0484/) - type hints and typing vocabulary.
- [PEP 621](https://peps.python.org/pep-0621/) - project metadata in `pyproject.toml`.
- [Python Packaging User Guide](https://packaging.python.org/) - packaging, dependency metadata, build backends, and distribution practices.
- [pytest documentation](https://docs.pytest.org/) - test discovery, fixtures, parametrization, and assertion style.
- [Ruff documentation](https://docs.astral.sh/ruff/) - linting and formatting rules for modern Python projects.
- [uv documentation](https://docs.astral.sh/uv/) - Python versions, virtual environments, dependency management, and command execution.
- [Pyright documentation](https://microsoft.github.io/pyright/) - static typing behavior and configuration.

## Books And Courses

- `Fluent Python` - idiomatic Python data model, functions, protocols, concurrency, and design patterns.
- `Effective Python` - practical guidance for readable, robust, modern Python.
- `Architecture Patterns with Python` - domain modeling, testing, dependency inversion, and application boundaries.
- `Python Testing with pytest` - focused pytest practice for fixtures, parametrization, and maintainable tests.

## Exemplary Projects

- [pytest](https://github.com/pytest-dev/pytest) - mature test framework architecture, plugin APIs, docs, and compatibility.
- [FastAPI](https://github.com/fastapi/fastapi) - typed API design, documentation, examples, and developer experience.
- [HTTPX](https://github.com/encode/httpx) - clean public API design, async/sync boundaries, tests, and transport abstraction.
- [Django](https://github.com/django/django) - long-term compatibility, documentation discipline, migrations, and project structure.
- [Pydantic](https://github.com/pydantic/pydantic) - typing-heavy API design, validation semantics, and performance trade-offs.

## What To Learn

- Keep public APIs typed and predictable; avoid unstructured dicts as long-lived domain models.
- Use exceptions deliberately: catch narrow exceptions, add context, and avoid silent failure.
- Prefer `pathlib`, context managers, dataclasses, enums, and clear module boundaries.
- Let `pyproject.toml`, `ruff`, `pytest`, and type checking define repeatable local and CI behavior.
- Design tests around behavior and edge cases rather than implementation details.

## Caveats

- Very mature projects may preserve old Python versions or legacy APIs; do not copy their compatibility compromises into new code.
- Framework repositories often include metaprogramming and plugin hooks that are unnecessary for ordinary application code.
- Tooling choices should follow the current repository unless the task is explicitly to modernize the toolchain.
