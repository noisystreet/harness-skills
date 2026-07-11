---
name: codebase-analysis
description: >-
  Analyze unfamiliar source codebases to build a reliable mental model: find
  entrypoints, map module boundaries and data flow, identify invariants and
  extension points, and produce a structured briefing. Use when onboarding to a
  repo, reading third-party library source, mapping architecture, or when the
  user mentions codebase analysis / source analysis / read the code /
  源码分析 / 读代码 / 摸清项目 / 模块关系.
  Bug investigation defers to debugging; PR critique defers to code-review;
  restructuring defers to refactoring.
---

# Codebase Analysis

目标是快速建立**可验证**的理解：系统从哪进、数据怎么流、边界在哪、哪里能安全改。
先地图，后细节；不确定就标注，不要编造。

落地样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 审查顺序

1. **定位**：这是什么、怎么构建/运行/测试
2. **入口**：进程、CLI、HTTP、worker、库公开 API
3. **骨架**：目录、模块依赖方向、核心类型
4. **主路径**：一条成功请求/任务/命令的端到端路径
5. **不变量与扩展点**：状态、错误、插件、配置
6. **输出**：结构化简报 + 不确定点 + 建议下一步

## 硬规则

1. **证据优先**：结论要能指向文件/符号/测试/文档；找不到就标 `uncertain`
2. **先跑通再深挖**：能构建/测试时先跑最小命令，用行为校正阅读
3. **一次一条主路径**：不要同时追所有子系统
4. **区分事实与推断**：推断必须写前提
5. **控制范围**：默认先画地图；用户未要求时不做大规模重构或风格重写

## 起步清单

按仓库已有材料读取（有则用，无则跳过）：

1. `README` / `AGENTS.md` / 架构文档 / ADR
2. 构建与质量入口：`Makefile`、`justfile`、`package.json`、`Cargo.toml`、`pyproject.toml`、CI
3. 目录顶层与包边界
4. 公开入口：`main`、路由表、worker 消费点、导出 API
5. 代表性测试：它们定义了「官方行为」

## 要画清的四张图

不必真画图，但简报里要覆盖：

1. **入口图**：谁启动、监听什么、配置从哪来
2. **模块图**：依赖方向；禁止的反向依赖若存在要指出
3. **数据流**：请求/事件/命令如何变成存储或外部调用
4. **状态归属**：可变状态在谁手里；跨边界如何传递

## 阅读策略

1. 自顶向下：入口 → 用例编排 → 领域逻辑 → 适配器/IO
2. 遇到框架魔法（反射、宏、DI、codegen）先找生成物或注册表，再读实现
3. 用测试和类型签名约束理解，比纯猜调用链更稳
4. 第三方代码优先读公开 API 与文档，再按需下钻实现
5. 大文件先搜符号/测试引用，避免线性通读

## 输出模板

```markdown
## Codebase Briefing

### Purpose
一句话：面向谁、解决什么

### How To Run
构建 / 测试 / 启动命令（或说明缺失）

### Entrypoints
- ...

### Module Map
- ...

### Primary Flow
端到端主路径（逐步，带关键文件）

### Invariants And Boundaries
状态、错误、鉴权、租户、幂等等

### Extension Points
插件、feature flag、注册表、配置开关

### Risks / Smells
有证据的风险；无证据不写

### Uncertainties
尚未证实的问题

### Suggested Next Steps
文档补齐 / 表征测试 / 针对性重构 / 继续深挖某子系统
```

## 与其他 skill 的边界

- 有失败症状要定位修复 → `debugging`
- 评价某次 diff/PR → `code-review`
- 行为不变的结构调整 → `refactoring`
- 领域不变量设计 → `data-modeling`
- 补架构/ADR 文档 → `docs-style`

## 禁止

- 在未定位入口前详述边角实现
- 把猜测写成确定事实
- 用「全面重写」代替分析结论
- 分析过程中无必要地大范围改代码
- 忽略仓库已有文档与测试给出的官方行为
