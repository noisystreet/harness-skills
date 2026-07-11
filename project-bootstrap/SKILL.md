---
name: project-bootstrap
description: >-
  Bootstrap new software projects with sensible modern defaults for tooling,
  layout, documentation, quality checks, tests, CI, and agent-facing docs.
  Use when creating a new project, initializing Python/Rust/C++ repositories,
  setting up pyproject/Cargo/CMake, AGENTS.md, LICENSE, SECURITY.md, or when the
  user mentions project bootstrap / 初始化项目 / 新项目脚手架.
  Language-specific conventions defer to python-style, rust-style, cpp-style,
  testing, secure-coding, and github-flow.
---

# Project Bootstrap

用于新项目初始化。目标是先建立可维护的最小工程骨架：项目定位、文档、格式化、lint、测试、安全基线、CI 入口。
落地样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 通用原则

1. 先写一句话定位：面向谁、解决什么问题、目标平台是什么
2. 新项目优先现代工具；既有项目不要强行迁移
3. 默认创建最小可运行示例、测试、README、忽略文件、环境模板和质量命令
4. 所有命令集中到一个入口：`justfile`、`Makefile`、`package scripts` 或项目惯用方式
5. 不引入重量级框架，除非用户明确需要

## 开题清单

新项目优先补齐这些文件（按规模裁剪）：

- `README.md`：项目是什么、如何安装/运行/测试、文档索引、许可证一句话
- `docs/ARCHITECTURE.md`：目标/非目标、模块边界、开放决策、目录规划
- `LICENSE`：明确许可证；公开项目优先使用 SPDX 标识
- `CONTRIBUTING.md`：贡献方式、测试/提交要求、安全问题不要公开报
- `SECURITY.md`：漏洞上报方式；暂未开放也要写清状态
- `CHANGELOG.md`：从 `[Unreleased]` 开始记录用户可见变更
- `AGENTS.md`：给 Agent 的项目身份、硬约束、验证命令和禁止事项
- `.env.example` + `.gitignore`：列出配置项，确保 `.env` 不入库
- `.editorconfig`：统一缩进、换行符和 UTF-8
- `.pre-commit-config.yaml`：提交前运行快速格式化、lint、密钥扫描和 commit-msg 检查（强烈推荐）

可直接参考模板：

- [templates/AGENTS.md](templates/AGENTS.md)
- [templates/ARCHITECTURE.md](templates/ARCHITECTURE.md)
- [templates/ADR.md](templates/ADR.md)
- [templates/PULL_REQUEST_TEMPLATE.md](templates/PULL_REQUEST_TEMPLATE.md)
- [templates/SECURITY.md](templates/SECURITY.md)
- [templates/CONTRIBUTING.md](templates/CONTRIBUTING.md)
- [templates/CHANGELOG.md](templates/CHANGELOG.md)
- [templates/env.example](templates/env.example) → 复制为 `.env.example`
- [templates/editorconfig](templates/editorconfig) → 复制为 `.editorconfig`
- [templates/pre-commit-config.yaml](templates/pre-commit-config.yaml) → 复制为 `.pre-commit-config.yaml`
- [templates/github-actions-ci.yml](templates/github-actions-ci.yml) → 复制为 `.github/workflows/ci.yml`

## 推荐组合

| 项目 | 默认工具 |
|------|----------|
| Python | `uv` + `ruff` + `pytest` + `pyright` |
| Rust | `cargo fmt` + `clippy` + `nextest` + `cargo deny` + `cargo machete` + `taplo` |
| C++ | CMake + `clang-format` + `clang-tidy` + CTest |

## Python 新项目

优先：

```bash
uv init
uv add --dev ruff pytest pyright
uv run ruff format .
uv run ruff check .
uv run pytest
uv run pyright
```

建议：

- 配置写入 `pyproject.toml`
- 源码放 `src/<package>/`，测试放 `tests/`
- 新代码默认类型标注；公开 API 必须标注
- CLI 项目使用 `project.scripts`

## Rust 新项目

优先：

```bash
cargo new <name>
cargo fmt
cargo clippy --all-targets --all-features -- -D warnings
cargo nextest run
cargo deny check
cargo machete
taplo fmt
```

建议：

- 新 crate 默认 2021+，能选新版本时优先 2024
- 库错误类型用 `thiserror`，应用层可用 `anyhow`
- CI 至少跑 fmt、clippy、test；安全/依赖检查按项目规模加入

## C++ 新项目

优先：

```bash
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build
ctest --test-dir build --output-on-failure
clang-format -i <files>
clang-tidy <files> -p build
```

建议：

- 新项目强烈推荐 CMake + `.clang-format`
- 开启 `compile_commands.json` 供 clangd/clang-tidy 使用
- 测试使用 CTest（具体测试框架按项目选择）
- 不把构建产物提交到仓库

## 质量入口

新项目尽量提供统一命令：

```bash
just fmt
just lint
just test
just check
```

没有 `just` 时可用 `make` 或项目既有脚本。重点是让 Agent 和人都知道该跑什么。

## 配置与依赖策略

1. 配置优先级写清：命令行参数 → 环境变量 → 配置文件 → 默认值
2. 敏感配置只通过环境变量或密钥管理服务注入
3. 锁文件策略写进 README/文档：应用/binary 通常提交锁文件；库按生态约定决定
4. dev-dependencies 只放测试、文档、lint 等开发期工具
5. 新增依赖需记录理由；重要选型用轻量 ADR（`docs/adr/0001-*.md`）

## CI 基线

最小 CI 应包含：

1. 格式检查
2. lint / 静态检查
3. 单元测试
4. 依赖/安全检查（项目面向生产或外部输入时）

本地强烈推荐配置 pre-commit，并与 CI 使用同一套检查入口。详细规则见 `ci-quality`。

## Agent 入口文档

`AGENTS.md` 至少写：

- 项目身份、技术栈、目录概览
- 模块依赖方向与禁止依赖
- 禁止引入的库/框架及原因
- Agent 可否修改架构文档、是否需要人工确认
- 安全红线：不得写入密钥、不得绕过权限检查
- 必跑验证命令：format/lint/test/type-check

## 禁止

- 新项目没有测试入口
- 新项目没有格式化/lint 入口
- 新项目没有 README 或最小可运行示例
- 为简单项目引入过重框架
- 把本地绝对路径写进配置
- 把密钥、真实 token、个人配置提交进仓库
