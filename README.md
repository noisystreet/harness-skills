# Harness Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-16-brightgreen.svg)](README.md)
[![CI](https://github.com/noisystreet/harness-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/noisystreet/harness-skills/actions/workflows/ci.yml)
[![AI Agents](https://img.shields.io/badge/AI%20Agents-Harness%20Skills-purple.svg)](README.md)
[![GitHub repo](https://img.shields.io/badge/GitHub-noisystreet%2Fharness--skills-black.svg)](https://github.com/noisystreet/harness-skills)

用于约束、编排和复用 AI 编程 Agent 的工程化 skills / 工作流规则集合。每个 skill 是一套可复用的指令，可被 Cursor、Claude Code、Codex、GitHub Copilot Chat 以及其他支持项目规则/上下文文件的编程 Agent 引用。

## 目录结构

```text
harness-skills/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .pre-commit-config.yaml
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── Makefile              # 安装 / 卸载 / 查看 / 校验 skill
├── api-design/           # API 契约、错误语义、分页、兼容性
│   ├── SKILL.md
│   └── examples.md
├── clean-code/           # 跨语言通用编程规范
│   └── SKILL.md
├── ci-quality/           # CI / pre-commit / 质量门禁
│   └── SKILL.md
├── code-review/          # 代码审查流程与输出格式
│   ├── SKILL.md
│   └── examples.md
├── commit-message/       # 提交信息规范
│   ├── SKILL.md
│   └── examples.md
├── debugging/            # 系统化排障流程
│   ├── SKILL.md
│   └── examples.md
├── development-workflow/ # 常用开发任务的 skill 路由
│   └── SKILL.md
├── docs-style/           # README / 架构 / ADR / CHANGELOG 文档规范
│   └── SKILL.md
├── github-flow/          # GitHub 协作流程
│   ├── SKILL.md
│   ├── reference.md      # 边界场景（rebase / 冲突 / draft 等）
│   └── templates/        # PR 正文模板
│       ├── pr-feature.md
│       ├── pr-bugfix.md
│       └── pr-hotfix.md
├── project-bootstrap/    # 新项目初始化建议
│   ├── SKILL.md
│   └── templates/        # AGENTS / 架构 / ADR / PR / 安全模板
│       ├── AGENTS.md
│       ├── ARCHITECTURE.md
│       ├── ADR.md
│       ├── PULL_REQUEST_TEMPLATE.md
│       └── SECURITY.md
├── runtime-reliability/  # 服务/Worker 运行时可靠性
│   ├── SKILL.md
│   └── examples.md
├── secure-coding/        # 通用安全编码基线
│   └── SKILL.md
├── rust-style/           # Rust 编程规范
│   └── SKILL.md
├── cpp-style/            # C++ 编程规范
│   └── SKILL.md
├── testing/              # 通用测试策略
│   ├── SKILL.md
│   └── examples.md
└── python-style/         # Python 编程规范
    └── SKILL.md
tools/
└── check_skills.py       # make check 使用的仓库校验脚本
```

每个 skill 至少包含一个 `SKILL.md`：

```text
skill-name/
├── SKILL.md              # 必需：指令主体（含 YAML frontmatter）
├── reference.md          # 可选：详细参考
├── examples.md           # 可选：示例
└── scripts/              # 可选：辅助脚本
```

## Skills 一览

<!-- BEGIN SKILLS CATALOG -->
| Skill | Description |
|-------|-------------|
| [`api-design`](api-design/) | Design and review APIs, including REST/HTTP, RPC, CLI-facing contracts, request/response schemas, error semantics, pagination, idempotency, versioning, compatibility, and OpenAPI/docs sync. Use when creating or changing endpoints, public interfaces, SDK contracts, webhooks, or when the user mentions API design / REST / OpenAPI / 接口设计. |
| [`ci-quality`](ci-quality/) | Design and review CI quality gates, local hooks, and repository checks for software projects. Use when setting up GitHub Actions/GitLab CI, pre-commit, format/lint/test/type-check workflows, dependency audits, coverage gates, or when the user mentions CI / pre-commit / quality gates / 持续集成. |
| [`clean-code`](clean-code/) | Apply language-agnostic clean code rules for readable, maintainable software. Use when writing, refactoring, or reviewing code of any language; when the user mentions clean code, readability, code quality, naming, or structure. Language-specific idioms defer to rust-style, cpp-style, python-style, or other *-style skills. |
| [`code-review`](code-review/) | Review code changes for correctness, regressions, maintainability, security, and test gaps. Use when reviewing pull requests, diffs, local changes, or when the user asks for code review / review / 审查 / 看看改动. Style-specific checks defer to clean-code and language *-style skills. |
| [`commit-message`](commit-message/) | Generate and review clear Conventional Commit messages from git diffs, staged changes, or change descriptions. Use when writing commits, reviewing commit history, choosing feat/fix/refactor/chore/test/docs types, or when the user mentions commit message / 提交信息 / 写提交. |
| [`cpp-style`](cpp-style/) | Apply modern C++ coding standards (C++17/20 idioms, RAII, safety, clarity). Use when writing, refactoring, or reviewing C++ code, CMake/Bazel C++ targets, or when the user mentions C++ style / guidelines / Modern C++ / CMake / clang-format / clang-tidy. General readability rules defer to clean-code; this skill owns C++-specific rules. |
| [`debugging`](debugging/) | Debug software failures systematically by reproducing, gathering evidence, narrowing hypotheses, and verifying fixes. Use when investigating bugs, failing tests, crashes, performance anomalies, flaky behavior, or when the user mentions debug / debugging / 排查 / 报错 / 失败. |
| [`development-workflow`](development-workflow/) | Route common software development tasks to the right combination of skills and execution order. Use when the user asks to develop, implement, refactor, fix bugs, review code, set up a project, write tests, prepare commits/PRs, or when the user mentions development workflow / 开发流程 / 按流程来. |
| [`docs-style`](docs-style/) | Write and review project documentation such as README, architecture docs, ADRs, CHANGELOG, AGENTS.md, SECURITY.md, API docs, and migration notes. Use when creating or updating docs, documenting code/API changes, writing release notes, or when the user mentions documentation / docs / README / ADR / CHANGELOG / 文档. |
| [`github-flow`](github-flow/) | Follow GitHub Flow for branching, commits, PRs, review, and merge. Use when creating branches, opening or updating pull requests, handling review comments, merging, resolving conflicts, or when the user mentions GitHub Flow / PR / MR / 开 PR / 提 PR / 合并分支 / 分支流程. |
| [`project-bootstrap`](project-bootstrap/) | Bootstrap new software projects with sensible modern defaults for tooling, layout, documentation, quality checks, tests, CI, and agent-facing docs. Use when creating a new project, initializing Python/Rust/C++ repositories, setting up pyproject/Cargo/CMake, AGENTS.md, LICENSE, SECURITY.md, or when the user mentions project bootstrap / 初始化项目 / 新项目脚手架. Language-specific conventions defer to python-style, rust-style, cpp-style, testing, secure-coding, and github-flow. |
| [`python-style`](python-style/) | Apply idiomatic modern Python coding standards with strong preference for uv, ruff, type hints, and pytest. Use when writing, refactoring, or reviewing Python code, or when the user mentions Python style / PEP 8 / type hints / pytest / uv / ruff. General readability rules defer to clean-code; this skill owns Python-specific rules. |
| [`runtime-reliability`](runtime-reliability/) | Design and review runtime reliability for long-running services, workers, CLIs, daemons, and networked systems. Use when implementing health checks, graceful shutdown, timeouts, retries, backoff, idempotency, queues, resource limits, observability, or when the user mentions reliability / runtime / health check / retry / timeout / worker / 稳定性. |
| [`rust-style`](rust-style/) | Apply Rust idioms and coding standards for idiomatic, safe, maintainable code. Use when writing, refactoring, or reviewing Rust code, Cargo projects, or when the user mentions Rust style / idioms / clippy / rustfmt / nextest / cargo deny. General readability rules defer to clean-code; this skill owns Rust-specific rules. |
| [`secure-coding`](secure-coding/) | Apply practical secure coding checks for application code, scripts, APIs, services, and automation. Use when writing or reviewing code that handles user input, authentication, authorization, secrets, files, shell commands, SQL/queries, network calls, logs, dependencies, or when the user mentions security / secure coding / 安全 / 漏洞 / 密钥. |
| [`testing`](testing/) | Design and improve tests for software changes, focusing on behavior, edge cases, regressions, and maintainable test structure. Use when writing tests, improving coverage, fixing flaky tests, or when the user mentions testing / test plan / pytest / cargo test / unit tests. Language-specific test tools defer to python-style, rust-style, cpp-style, etc. |
<!-- END SKILLS CATALOG -->

## 如何使用

### 推荐组合

| 场景 | 推荐组合 |
|------|----------|
| 写 Python | `clean-code` + `python-style` + `testing` + `secure-coding` |
| 写 Rust | `clean-code` + `rust-style` + `testing` + `secure-coding` |
| 写 C++ | `clean-code` + `cpp-style` + `testing` |
| 设计/修改 API | `api-design` + `secure-coding` + `testing` + `docs-style` |
| 服务 / Worker | `runtime-reliability` + `secure-coding` + `testing` + `ci-quality` |
| 审 PR / diff | `code-review` + `clean-code` + `testing` + `secure-coding` + `ci-quality` |
| 排查 bug | `debugging` + `testing` |
| 提 PR | `github-flow` + `commit-message` + `ci-quality` |
| 写/改文档 | `docs-style` |
| 新项目初始化 | `project-bootstrap` + `docs-style` + `ci-quality` + 对应语言 `*-style` |
| 不确定该用什么 | `development-workflow` |

### 常用触发语

- 「按 `code-review` 审查这次改动」
- 「按 `api-design` 设计这个接口」
- 「按 `python-style` 写这个模块」
- 「按 `debugging` 帮我排查这个失败」
- 「按 `development-workflow` 实现这个功能」
- 「按 `docs-style` 更新 README 和 ADR」
- 「按 `runtime-reliability` 检查这个 worker」
- 「按 `testing` 给这个 bug 补回归测试」
- 「按 `github-flow` 开 PR」
- 「按 `ci-quality` 配置 CI 和本地检查」
- 「按 `project-bootstrap` 初始化一个 Rust/Python/C++ 项目」

### 通用用法

这些 skill 本质上是 Markdown 指令文件。不同 AI 编程工具可以用不同方式引用：

| 工具类型 | 使用方式 |
|----------|----------|
| 支持 Skills 目录的工具 | 将需要的 skill 目录复制或符号链接到该工具的 skills 目录 |
| 支持 `AGENTS.md` / `CLAUDE.md` / 项目规则的工具 | 在项目规则文件里引用本仓库对应 `SKILL.md`，或复制精简规则 |
| Chat/CLI 类工具 | 在任务中明确说「按 `<skill-name>`」，并附上或让工具读取对应 `SKILL.md` |
| 不支持自动发现的工具 | 手动把相关 `SKILL.md` 内容作为上下文提供 |

推荐先使用 `development-workflow` 做路由，再按任务读取具体 skill。

### 项目内引用

把需要的 skill 链到或复制到目标项目的 AI 工具规则目录。示例：

```bash
# 例：某工具支持 .ai/skills/
mkdir -p /path/to/your-project/.ai/skills
ln -s "$(pwd)/rust-style" /path/to/your-project/.ai/skills/rust-style

# 或直接复制
cp -r github-flow /path/to/your-project/.ai/skills/
```

如果工具约定了特定目录（如 `.cursor/skills/`），把上面的 `.ai/skills/` 换成对应目录即可。

### 个人全局 Skills

默认 `make install` 会把 skill 链接到 Cursor 兼容目录 `~/.cursor/skills/`。这只是一个默认安装目标；其他工具可通过 `SKILLS_DIR` 指定目标目录：

```bash
make install

# 安装到自定义 skills 目录
make install SKILLS_DIR=/path/to/your-ai-tool/skills
```

查看链接状态：

```bash
make list
```

校验 skill 元数据与 README：

```bash
make check
```

卸载本仓库创建的链接：

```bash
make uninstall

# 卸载自定义目标目录中的链接
make uninstall SKILLS_DIR=/path/to/your-ai-tool/skills
```

> 如果使用 Cursor，不要放到 `~/.cursor/skills-cursor/`，那是 Cursor 内置 skill 目录。

### 其他 AI 编程工具示例

**Claude Code / 支持 `CLAUDE.md` 的工具**

在项目 `CLAUDE.md` 中写：

```markdown
开发任务优先参考：
- /path/to/skills/development-workflow/SKILL.md
- /path/to/skills/clean-code/SKILL.md
- /path/to/skills/testing/SKILL.md

按任务类型再读取对应语言或领域 skill。
```

**Codex / 通用 CLI Agent**

在提示词中写：

```text
请按 /path/to/skills/development-workflow/SKILL.md 分析任务，
涉及 Python 时再参考 /path/to/skills/python-style/SKILL.md。
```

**GitHub Copilot Chat / IDE 规则**

把常用 skill 的要点复制到项目规则、仓库说明或 `AGENTS.md`，并保留到本仓库 `SKILL.md` 的链接，避免多处规则漂移。

### 在对话中使用

- 支持自动发现的工具会根据 `SKILL.md` 的 `description` 匹配相关 skill
- 也可在对话里直接点名，例如：「按 rust-style 写这段代码」

## 新增 Skill

1. 新建目录：`mkdir skill-name`
2. 创建 `SKILL.md`，包含 frontmatter：

```markdown
---
name: skill-name
description: 一句话说明做什么、何时使用（Agent 靠这段决定是否启用）
---

# Skill Name

具体指令……
```

3. `description` 写清楚触发条件；正文只写 Agent 执行时需要的规则，避免空话
4. 运行 `make catalog` 更新 README skill 目录
5. 运行 `make check`

## 维护流程

修改或新增 skill 时：

1. 优先修改已有 skill；只有职责不同或触发场景明显不同才新增
2. `SKILL.md` 保持精简，原则上少于 500 行；长细节放一层 `reference.md` / `examples.md`
3. 工具链建议区分「新项目强烈推荐」和「既有项目跟随」
4. 不写真实本机路径、密钥、账号信息或公司内部地址
5. 用户可见变更同步 `CHANGELOG.md`
6. 修改后运行：

```bash
make catalog
make check
make install
```

## 约定

- 目录名使用 `kebab-case`
- `name` 与目录名保持一致
- 一个 skill 只做一件事；规范类与流程类分开
- 优先写「必须 / 禁止」规则，少写背景介绍
