---
name: refactoring
description: >-
  Perform safe, behavior-preserving refactors in small verified steps with
  characterization tests, clear seams, and minimal blast radius. Use when
  restructuring code, reducing complexity, extracting modules, renaming across
  boundaries, paying down tech debt, or when the user mentions refactor /
  refactoring / 重构 / 整理代码 / strangler.
  Style rules defer to clean-code and language *-style skills; bug fixes that
  change behavior are not pure refactors.
---

# Refactoring

重构默认保持可观察行为不变。先让改动可安全移动，再谈更漂亮的结构。

落地样例见 [examples.md](examples.md)。

## 审查顺序

1. **目标**：要降低什么复杂度、方便什么后续改动
2. **安全网**：有没有表征测试/回归测试锁住当前行为
3. **切片**：能否拆成可复查的小步
4. **验证**：每步后测试/类型检查仍绿
5. **收尾**：API/文档/命名是否与新结构一致，无行为变化混入

## 硬规则

1. **行为不变**：纯重构 PR/提交不要夹带功能或修 bug；必须夹带时在说明里显式拆分
2. **先测后动**：关键路径缺少测试时，先补表征测试或最小固定输入/输出
3. **小步提交**：提取、改名、移文件、改接口分层进行，避免巨型「整理」
4. **先找接缝**：通过接口、纯函数、适配层隔离，再替换内部
5. **保留可回滚**：每步应能单独回退；不要一次改完才第一次运行测试

## 常用安全手法

- 提取函数/模块，不改变外部契约
- 引入适配层（strangler）：新旧实现并存，逐步切流
- 扩展再收缩：先加新接口，迁移调用方，再删旧接口
- 用类型/枚举显式化隐式状态（配合 `clean-code`）
- 数据与格式转换集中到边界，内部用统一模型
- 引入模式前先证明复杂度：为策略/适配而提取，不为「套模式」而提取（见 `clean-code`）
- 边界或依赖方向调整时对照 `software-architecture`，避免只搬家不改依赖规则

## 表征测试

对遗留代码：

1. 固定代表性输入，锁定当前输出/副作用
2. 覆盖成功路径、关键边界、已知怪异行为
3. 测试名写清「当前行为是什么」，不要美化成理想行为
4. 重构完成后，若要改变行为，另开变更并更新测试

## PR 与提交建议

1. PR 描述写：重构动机、不变的行为、验证命令、风险点
2. 大范围改名/移文件尽量独立提交，减少 review 噪音
3. 生成代码/格式化与逻辑结构调整分开
4. 若影响公共 API，明确兼容策略；破坏性变更走 `api-design` / 文档流程

## 风险信号（停下拆分）

- 无法解释如何验证行为不变
- 同时改数据结构、控制流和外部 API
- 删除「好像没用」的代码却无引用证明/测试
- 重构范围跨多个无关子系统

## 与其他 skill 的边界

- 命名、状态、函数职责、模式取舍 → `clean-code`
- 语言惯用法 → 对应 `*-style`
- 行为变更与回归 → `testing`
- 接口兼容 → `api-design`
- 模块边界与架构风格 → `software-architecture`
- 性能动机的结构变化 → 先 `performance` 证明热点

## 禁止

- 「顺便」重构整棵目录树
- 无测试大改遗留模块
- 把重构当借口重写系统
- 用重构提交隐藏行为变化
- 在红灯测试上继续大范围搬移
- 为套设计模式而增加无收益的间接层
