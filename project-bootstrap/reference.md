# Project Bootstrap References

## Tooling Docs

- [uv](https://docs.astral.sh/uv/) / [ruff](https://docs.astral.sh/ruff/) / [pytest](https://docs.pytest.org/) - Python defaults.
- [Cargo Book](https://doc.rust-lang.org/cargo/) / [Clippy](https://doc.rust-lang.org/clippy/) / [nextest](https://nexte.st/) - Rust defaults.
- [CMake](https://cmake.org/cmake/help/latest/) / [clang-format](https://clang.llvm.org/docs/ClangFormat.html) - C++ defaults.
- [pre-commit](https://pre-commit.com/) / [EditorConfig](https://editorconfig.org/) - editor and hook baselines.
- [Keep a Changelog](https://keepachangelog.com/) / [ADR](https://adr.github.io/) - docs baselines.

## What To Learn

- Prefer a thin, runnable skeleton over a framework museum.
- Put commands in one entrypoint agents can discover.
- Security and contribution docs are part of bootstrap, not later chores.

## Markdown Line Width

Agent 读取、grep 和 diff 都按行处理。一行塞满整段会让输出被截断，也让 review 只能看到
首屏。`templates/check_markdown_width.py` 默认限制 120 显示列，CJK 字符按 2 列计算。

以下内容不检查：

- YAML frontmatter、fenced code block、表格行
- 整行只有一个 badge / 图片 / 链接 / 裸 URL
- 仅因不可断行 URL 超限，且总宽不超过 300 列的行

复制到 `tools/check_markdown_width.py` 后，在 `make check` / `just check` 和 pre-commit
中调用。需要更宽的表格时优先拆列，而不是放宽阈值。这个规则约束的是 prose，无法防止
工具在超大单行上截断；真遇到超长单行，应该拆段落或拆表格。

## Caveats

- Existing organizations may mandate different scaffolds; adapt rather than fight local standards on day one.
