---
name: development-workflow
description: >-
  Route common software development tasks to the right combination of skills
  and execution order. Use when the user asks to develop, implement, refactor,
  fix bugs, review code, set up a project, write tests, prepare commits/PRs,
  or when the user mentions development workflow / 开发流程 / 按流程来.
---

# Development Workflow

本 skill 只负责编排，不重复具体规则。需要细节时使用对应 skill。

## 路由表

| 任务 | 组合 |
|------|------|
| 新项目初始化 | `project-bootstrap` → 对应语言 `*-style` → `testing` → `secure-coding` → `ci-quality` |
| 写新功能 | `clean-code` → 对应语言 `*-style` → `testing` → `secure-coding` |
| 设计/修改 API | `api-design` → `secure-coding` → `testing` → `docs-style` |
| 长期运行服务/Worker | `runtime-reliability` → `secure-coding` → `testing` → `ci-quality` |
| 修 bug | `debugging` → `testing` → `clean-code` → 对应语言 `*-style` |
| 重构 | `clean-code` → 对应语言 `*-style` → `testing` |
| 审 PR / diff | `code-review` → `testing` → `secure-coding` → `ci-quality` |
| 配 CI / 质量门禁 | `ci-quality` → `testing` → `secure-coding` |
| 写/改文档 | `docs-style` → `project-bootstrap`（新项目） |
| 提交 / 开 PR | `commit-message` → `github-flow` |

## 执行原则

1. 先识别任务类型、语言、仓库阶段（新项目 / 既有项目 / PR 中）
2. 选择最小必要 skill 组合；不要为简单问题加载全部规则
3. 语言规则只从对应 `*-style` 取；跨语言规则从 `clean-code` 取
4. 有安全、外部输入、权限、密钥、网络、文件或 shell 调用时加入 `secure-coding`
5. 涉及接口、SDK、CLI 参数、webhook、错误语义、分页或版本兼容时加入 `api-design`
6. 涉及长期运行服务、worker、队列、健康检查、超时、重试或资源上限时加入 `runtime-reliability`
7. 有行为变化时加入 `testing`
8. 涉及 README、架构、ADR、CHANGELOG、AGENTS 或迁移说明时加入 `docs-style`
9. 涉及协作、提交、PR 时加入 `commit-message` 和 `github-flow`

## 常见流程

### 新项目

1. 用 `project-bootstrap` 建立 README、最小工程、工具链、测试入口、AGENTS
2. 用语言 `*-style` 选择默认工具和代码规范
3. 用 `testing` 确定测试分层
4. 用 `secure-coding` 建立 `.env.example`、安全上报和输入边界
5. 用 `docs-style` 生成/维护 README、架构文档、ADR、CHANGELOG 和 AGENTS
6. 用 `ci-quality` 配置 format/lint/test/security 门禁

### 实现功能

1. 明确行为与边界
2. 用 `clean-code` 和语言 `*-style` 实现
3. 用 `testing` 补测试
4. 若涉及输入/权限/密钥/外部调用，用 `secure-coding` 检查
5. 若涉及 API 契约，用 `api-design` 检查错误语义、兼容性和文档
6. 若涉及长期运行行为，用 `runtime-reliability` 检查超时、重试、关闭和观测
7. 若用户可见行为/API/配置变化，用 `docs-style` 同步文档
8. 准备提交时用 `commit-message`

### 修 bug

1. 用 `debugging` 复现与定位根因
2. 用 `testing` 先补回归测试或最小复现
3. 修复时遵循 `clean-code` 和语言 `*-style`
4. 用 `code-review` 视角检查是否引入回归

### 审查改动

1. 用 `code-review` 先找 correctness / regression / test gap
2. 用 `secure-coding` 检查敏感输入、权限和泄漏
3. 用 `testing` 判断测试是否够
4. 用 `ci-quality` 检查门禁是否覆盖

## 禁止

- 把本 skill 写成所有规则的大合集
- 只调用 meta skill 却忽略对应具体 skill
- 为小任务套完整新项目流程
- 在没有证据时跳过 `debugging` 直接大改
