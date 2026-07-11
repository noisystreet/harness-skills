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

| Skill | 用途 | 触发场景 |
|-------|------|----------|
| [`api-design`](api-design/) | API 契约、错误语义、分页、兼容性 | 设计/修改接口、OpenAPI、SDK、webhook |
| [`clean-code`](clean-code/) | 跨语言可读性 / 可维护性规范 | 编写、重构、审查任意语言代码 |
| [`ci-quality`](ci-quality/) | CI / pre-commit / 质量门禁 | 配置 CI、pre-commit、format/lint/test 检查 |
| [`code-review`](code-review/) | 代码审查流程与输出格式 | 审查 PR、diff、本地改动 |
| [`commit-message`](commit-message/) | Conventional Commits 提交信息规范 | 写提交信息、审查提交历史、选择 type |
| [`debugging`](debugging/) | 系统化排障流程 | 报错、失败测试、偶现问题、性能异常 |
| [`development-workflow`](development-workflow/) | 常用开发任务的 skill 路由 | 开发、实现、修 bug、审查、提 PR、新项目 |
| [`docs-style`](docs-style/) | README / 架构 / ADR / CHANGELOG 文档规范 | 写文档、更新文档、API 迁移、发布说明 |
| [`github-flow`](github-flow/) | GitHub 协作流程（分支、PR、review、合并） | 提 PR、处理 review、分支管理 |
| [`project-bootstrap`](project-bootstrap/) | 新项目初始化建议 | 初始化 Python / Rust / C++ 项目、配置工具链 |
| [`runtime-reliability`](runtime-reliability/) | 服务/Worker 运行时可靠性 | 健康检查、优雅退出、超时、重试、背压 |
| [`secure-coding`](secure-coding/) | 通用安全编码基线 | 密钥、输入、权限、注入、日志、依赖风险 |
| [`rust-style`](rust-style/) | Rust 编程规范与惯用法 | 编写 / 审查 Rust 代码 |
| [`cpp-style`](cpp-style/) | C++ 编程规范与惯用法 | 编写 / 审查 C++ 代码 |
| [`testing`](testing/) | 通用测试策略 | 写测试、补覆盖、修 flaky test |
| [`python-style`](python-style/) | Python 编程规范与惯用法 | 编写 / 审查 Python 代码 |

按需继续追加，例如：`commit-message`、`code-review` 等。

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
4. 在本 README 的表格里登记一行
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
make check
make install
```

## 约定

- 目录名使用 `kebab-case`
- `name` 与目录名保持一致
- 一个 skill 只做一件事；规范类与流程类分开
- 优先写「必须 / 禁止」规则，少写背景介绍
