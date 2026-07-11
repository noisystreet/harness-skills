---
name: docs-style
description: >-
  Write and review project documentation such as README, architecture docs,
  ADRs, CHANGELOG, AGENTS.md, SECURITY.md, API docs, and migration notes.
  Use when creating or updating docs, documenting code/API changes, writing
  release notes, or when the user mentions documentation / docs / README /
  ADR / CHANGELOG / 文档.
---

# Docs Style

文档服务于决策、使用和协作。少写空话，多写读者需要执行或判断的信息。

## 总原则

1. 先明确读者：用户、开发者、维护者、审阅者、Agent
2. 先写事实和约束，再写背景故事
3. 文档与代码单一信息源；不要在多个地方复制同一规则
4. 行为/API/配置变化必须同步相关文档，或说明无需更新
5. 示例要能运行或明确是伪代码

## README

README 应回答：

1. 这是什么，解决什么问题
2. 如何安装 / 运行 / 测试
3. 最小示例或快速开始
4. 文档索引
5. 许可证和贡献入口

避免：

- 营销式夸张描述
- 只有愿景，没有运行命令
- 过长，把架构细节全部塞进 README

## 架构文档

`docs/ARCHITECTURE.md` 应包含：

- 目标与非目标
- 模块边界和依赖方向
- 关键数据模型 / 外部系统
- 配置优先级
- 安全边界
- 开放决策

重大设计变化用 ADR 记录，不把历史决策埋在 PR 评论里。

## ADR

ADR 适用于不可轻易反悔的工程决策：框架、存储、协议、部署模型、兼容性策略。

结构：

```markdown
# ADR: [Title]

## Status
Proposed / Accepted / Superseded

## Context
为什么需要决策，约束是什么

## Decision
选择了什么

## Consequences
好处、代价、后续约束

## Alternatives Considered
比较过但未选择的方案
```

## CHANGELOG

默认采用 Keep a Changelog 风格：

```markdown
## [Unreleased]

### Added
### Changed
### Fixed
### Removed
### Security
```

- 只记录用户/维护者关心的变化，不记录每个内部提交
- 破坏性变更必须写迁移说明或链接
- 安全修复放 `Security`

## AGENTS.md

给 Agent 的文档应短、硬、可执行：

- 项目身份和技术栈
- 目录结构概览
- 禁止依赖 / 依赖方向
- 安全红线
- 必跑命令
- 哪些文档可改、哪些需人工确认

不要把全部规范复制进 `AGENTS.md`；链接到 README、架构文档或本仓库 skill。

## API / 迁移文档

API 变化应说明：

- 请求/响应或函数签名变化
- 错误语义
- 兼容性影响
- 迁移步骤
- 示例

弃用流程要写清：何时标记 deprecated、何时移除、替代方案是什么。

## 语言与风格

1. 标题具体，不用「其它」「注意事项」这类大筐
2. 步骤用编号；并列规则用短列表
3. 命令可复制，避免本机绝对路径
4. 链接到具体文件，不链接不存在的未来文档
5. 中英文文档若并存，改一边要同步另一边或明确占位

## 禁止

- 文档声称支持但代码/CI 不支持
- 写真实密钥、内部 URL、个人路径
- 用长篇背景掩盖缺少操作步骤
- API 破坏性变化没有 CHANGELOG/迁移说明
- 复制多个来源导致规则漂移
