---
name: data-modeling
description: >-
  Design and review domain data models, invariants, boundaries, identity keys,
  consistency expectations, and persistence mapping. Use when defining entities,
  aggregates, schemas, idempotency keys, state transitions, or when the user
  mentions data modeling / domain model / invariant / aggregate / 数据模型 /
  不变量 / 一致性.
  HTTP/API shapes defer to api-design; migration mechanics defer to migration.
---

# Data Modeling

先把业务不变量与边界说清，再落到表结构或 API 字段。模型要表达规则，不只是存字段。

落地样例见 [examples.md](examples.md)。

## 审查顺序

1. **概念**：有哪些实体、值对象、生命周期
2. **不变量**：什么必须永远为真
3. **边界**：事务/一致性边界在哪里
4. **身份与引用**：主键、业务键、幂等键
5. **状态**：合法迁移，而不是散落布尔

## 硬规则

1. **显式不变量**：金额非负、唯一邮箱、订单状态机等写进模型/校验/测试
2. **边界内强一致，边界外最终一致**：跨服务/跨聚合不要假装同一本地事务
3. **用业务键表达幂等**：创建/支付/导入有稳定去重键
4. **状态用枚举/代数类型**：禁止多布尔伪装生命周期
5. **区分身份与属性**：可变展示名不是身份；id 稳定，不要用可变字段当主键

## 实体与值对象

1. 实体有稳定身份；值对象按值相等（如 Money、Email）
2. 不要把所有东西都建成可变实体
3. 聚合根控制内部一致性；外部只通过根或明确应用服务操作
4. 引用其他聚合用 id，不直接持有可变内部对象图（跨边界）

## 一致性与事务

1. 单个用例尽量落在一个一致性边界内
2. 跨边界用发件箱/消息/工作流，并定义重试与补偿
3. 读写模型可分离，但要声明延迟与正确性期望
4. 「先写 A 再写 B」失败时的部分完成状态必须可恢复或可检测

## 键与约束

1. 技术主键与业务唯一约束分开设计
2. 幂等键范围写清：按用户、按租户、还是全局
3. 软删除要定义唯一约束与恢复语义，避免「删了还能再插同键」的坑
4. 时间字段区分 event time / processing time；时区策略明确

## 持久化映射

1. 表/集合是模型的一种投影，不要让 DB 列名反向污染领域语言（可接受翻译层）
2. 约束能下沉数据库的（唯一、外键、非空）优先双保险
3. 序列化 JSON blob 前问：哪些字段需要查询、约束、迁移
4. 大对象/冷热数据分离，避免核心行无限膨胀

## 与 API 的关系

1. API DTO ≠ 领域模型；可转换，但不要把存储结构直接当公共契约
2. 对外暴露的状态与错误码要稳定（见 `api-design`）
3. 分页排序字段必须是模型中有定义的稳定键

## 与其他 skill 的边界

- REST/错误/版本 → `api-design`
- 表结构变更步骤 → `migration`
- 隐式状态与命名 → `clean-code`
- 并发下的共享可变数据 → `clean-code` 并发章节与语言 `*-style`

## 禁止

- 用可空字段堆出隐式状态机
- 跨服务分布式大事务硬撑「强一致」
- 无业务键的可重复金融/创建操作
- 把所有关系塞进一个超级大表/大对象
- 不写不变量却指望调用方「小心使用」
