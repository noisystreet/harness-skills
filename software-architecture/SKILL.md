---
name: software-architecture
description: >-
  Design and review software architecture: quality attributes, module
  boundaries, dependency rules, and architecture style trade-offs. Use when
  choosing layering, hexagonal/clean architecture, modular monoliths, event-
  driven split, or when the user mentions software architecture / system design /
  module boundaries / 软件架构 / 分层 / 六边形 / 架构风格.
  ADR writing defers to docs-style; domain aggregates defer to data-modeling;
  safe structural change defers to refactoring; GoF tactics defer to clean-code.
---

# Software Architecture

架构回答「系统如何切分与协作」，服务明确的质量属性。先约束与边界，再选风格；不为时髦结构付税。

落地样例见 [examples.md](examples.md)。经典参考见 [reference.md](reference.md)。

## 审查顺序

1. **目标与非目标**：系统为谁服务，明确不做什么
2. **质量属性**：可维护、可测、性能、安全、可运维等优先级
3. **边界**：模块/限界上下文、所有权、依赖方向
4. **风格**：分层、六边形、模块化单体、事件驱动等是否匹配约束
5. **演进**：如何发布、迁移、回滚；是否需要 ADR

## 硬规则

1. **质量属性驱动**：每个重大结构选择都要对应可陈述的属性（例如独立部署、测试隔离、故障隔离）
2. **依赖单向**：内层/领域不依赖框架与 IO 细节；允许的依赖方向写进架构文档
3. **边界对齐变更频率与所有权**：一起变的放一起，跨团队契约显式化
4. **先模块化单体，再拆服务**：没有独立伸缩/故障/发布需求时，不要默认微服务
5. **重要选择记 ADR**：见 `docs-style`；聊天结论不算架构决策

## 质量属性（先排序）

常见需要显式取舍：

- 可变更性 / 可理解性
- 可测试性
- 性能与容量
- 可用性与故障隔离
- 安全性与审计
- 可观测性与可运维性
- 交付速度（团队认知负荷）

属性冲突时写清优先级，不要假装全都第一。

## 边界与依赖

1. 按领域能力或业务价值切，不按技术层无限切碎（`controllers/` 全家桶除外已有约定时）
2. 公开表面小而稳；内部结构可动
3. 禁止「工具库」变成隐式中心依赖
4. 跨边界通信用明确 DTO/事件/API，不共享可变内部模型
5. 循环依赖视为设计失败，优先拆接口或反转依赖

## 架构风格选用

| 风格 | 更适合 | 慎用当 |
|------|--------|--------|
| 分层 | 简单应用、清晰 IO/领域分界 | 跨层偷调、事务脚本膨胀 |
| 六边形 / ports-adapters | 领域稳定、适配器多变 | 样板多于业务的小脚本 |
| 模块化单体 | 团队中小、需强模块边界 | 模块边界只停在目录名 |
| 事件驱动 | 异步解耦、最终一致可接受 | 强一致流程却靠「多事件碰运气」 |
| 微服务 | 独立发布/伸缩/故障隔离刚需 | 组织与观测未就绪就拆 |

选风格时写清：**得到什么、付出什么、拒绝什么替代方案**。

## 与代码结构

1. 目录与包名反映边界，不反映临时个人习惯
2. 应用服务编排用例；领域表达不变量（配合 `data-modeling`）
3. 基础设施（DB、HTTP、消息）可替换，不泄漏进领域核心
4. 具体类结构手法（Strategy/Adapter 等）→ `clean-code` / `refactoring`

## 输出建议

架构讨论结束时应有其一：

- 更新 `ARCHITECTURE.md` 的目标/边界/依赖图
- 新增或修订 ADR
- 明确「暂不改变」及原因

## 与其他 skill 的边界

- ADR 文风与模板 → `docs-style`
- 领域不变量 / 聚合 → `data-modeling`
- 读现有结构 → `codebase-analysis`
- 行为不变落地改造 → `refactoring`
- 接口契约 → `api-design`
- 运行时与开关 → `runtime-reliability`

## 禁止

- 无质量属性的「先上微服务/先上 DDD」
- 复制一套分层目录却允许任意跨层调用
- 把架构讨论只留在口头，不更新文档/ADR
- 用设计模式清单代替边界与依赖规则
