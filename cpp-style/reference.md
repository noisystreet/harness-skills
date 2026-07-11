# C++ Style References

Use these references as calibration points when applying `cpp-style`. C++ style is especially project-dependent; follow the repository's standard version, formatter, exception policy, and ownership conventions first.

## Official And Community Guides

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) - broad modern C++ guidance for interfaces, resources, ownership, errors, and concurrency.
- [cppreference](https://en.cppreference.com/) - standard library and language reference.
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) - pragmatic large-codebase style guidance; useful as a comparison point, not universal law.
- [LLVM Coding Standards](https://llvm.org/docs/CodingStandards.html) - production C++ style for a large compiler ecosystem.
- [CMake documentation](https://cmake.org/cmake/help/latest/) - modern CMake targets, properties, dependencies, and build configuration.
- [clang-format documentation](https://clang.llvm.org/docs/ClangFormat.html) - formatting configuration and behavior.
- [clang-tidy documentation](https://clang.llvm.org/extra/clang-tidy/) - static checks for modernize, readability, bugprone, and performance concerns.

## Books And Courses

- `Effective Modern C++` - move semantics, type deduction, smart pointers, lambdas, and concurrency-era idioms.
- `C++ Core Guidelines Explained` - practical interpretation of the Core Guidelines.
- `A Tour of C++` - compact overview of modern language and standard library features.
- `Large-Scale C++ Software Design` - dependency management, physical design, and large-codebase maintainability.
- `C++ Concurrency in Action` - thread safety, atomics, locks, and concurrency design.

## Exemplary Projects

- [LLVM](https://github.com/llvm/llvm-project) - large-scale C++ architecture, tooling, diagnostics, and long-term maintainability.
- [fmt](https://github.com/fmtlib/fmt) - modern C++ API design, type safety, formatting, and tests.
- [Catch2](https://github.com/catchorg/Catch2) - header/library organization, test ergonomics, and CMake integration.
- [Protocol Buffers](https://github.com/protocolbuffers/protobuf) - cross-language API compatibility, build complexity, and generated-code boundaries.
- [Abseil](https://github.com/abseil/abseil-cpp) - reusable library design, compatibility, and careful standard-library-adjacent abstractions.

## What To Learn

- Make ownership and lifetime explicit with RAII, values, references, and smart pointers.
- Prefer stable interfaces and narrow headers; manage include dependencies intentionally.
- Keep exception policy consistent across a project instead of mixing incompatible error styles.
- Use `enum class`, `optional`, `expected` or project error types to express states and failure explicitly.
- Treat `clang-format`, `clang-tidy`, CMake configuration, and tests as part of the style baseline.

## Caveats

- Some high-profile projects intentionally avoid exceptions, RTTI, or parts of the standard library; copy those choices only when your project has the same constraints.
- C++ standards evolve quickly; do not force C++20/23 idioms into a C++17 codebase unless the project is moving there.
- Performance-sensitive libraries may use complexity that is inappropriate for ordinary application code.
