---
name: migration
description: >-
  Plan and execute safe schema, data, API, and config migrations with
  expand/contract steps, compatibility windows, rollback, and verification.
  Use when changing databases, message formats, public APIs, feature cutovers,
  or when the user mentions migration / expand-contract / backfill / 迁移 /
  兼容窗口 / 回滚迁移.
  API contract details defer to api-design; release cutover defers to release.
---

# Migration

迁移默认假设旧版本与新版本会短暂共存。先扩容兼容，再切换，最后收缩清理。

落地样例见 [examples.md](examples.md)。

## 审查顺序

1. **变更类型**：schema、数据回填、API、配置、消息格式、存储引擎
2. **兼容窗口**：谁在读旧、谁在写新，共存多久
3. **步骤**：expand → migrate/backfill → switch → contract
4. **验证**：正确性、性能、回滚点
5. **清理**：何时删除旧字段/旧路径，谁负责

## 硬规则

1. **向前兼容优先**：旧客户端/旧 worker 在窗口期内不能被新格式直接打挂
2. **可回滚**：每个不可逆步骤前有明确回滚或补偿方案；无法回滚要写清风险与人工恢复
3. **小步可观察**：每步可单独部署/验证；禁止「改库+改代码+删旧字段」一次做完
4. **双写/双读要有退出条件**：完成标准、监控指标、截止日期
5. **破坏性 API 变更**必须有版本/弃用窗口与迁移文档（配合 `api-design` / `docs-style`）

## Expand / Contract

典型顺序：

1. **Expand**：新增字段/表/topic/处理器，旧代码仍可用
2. **Migrate**：回填历史数据；校验新旧等价
3. **Switch**：切读或切写到新路径（可灰度）
4. **Contract**：确认无旧依赖后删除旧字段/旧代码/旧索引

禁止在 Expand 未完成时做 Contract。

## 数据与 Schema

1. 新增列优先可空或带默认；避免一开始 NOT NULL 无默认导致锁表/失败
2. 大表变更评估锁、耗时、在线 DDL/分批回填
3. 回填任务可恢复、可限流，记录进度与失败行
4. 校验用抽样 + 关键不变量全量检查（按成本选择）
5. 删除列/改类型前确认代码路径与离线作业都已迁移

## API / 消息格式

1. 新字段通常可选；删除/改语义走弃用期
2. 消费者先兼容新旧，再生产端切换
3. 消息 schema 变更保留版本号或等价判别字段
4. 幂等键与去重策略在迁移期保持有效

## 验证与回滚

每步至少验证：

- 功能正确：抽样对比或差分
- 错误率/延迟未明显恶化
- 回滚演练或文档化的回滚命令

回滚策略写清：代码回滚是否足够，是否需要数据补偿。

## 文档

迁移说明至少包含：

- 背景与影响面
- 步骤时间表与负责人
- 兼容窗口起止
- 验证命令/指标
- 回滚步骤
- 清理截止条件

## 与其他 skill 的边界

- 接口契约与版本策略 → `api-design`
- 发布 tag/灰度/回滚清单 → `release`
- 特性开关切流 → `runtime-reliability`（特性开关章节）
- 领域不变量 → `data-modeling`

## 禁止

- 生产一次性「大爆炸」迁移无窗口
- 未验证回填完成就删除旧数据
- 只迁移在线路径，忘记批处理/报表/脚本
- 把迁移细节只留在聊天记录里
