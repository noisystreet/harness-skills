---
name: runtime-reliability
description: >-
  Design and review runtime reliability for long-running services, workers,
  CLIs, daemons, and networked systems. Use when implementing health checks,
  graceful shutdown, timeouts, retries, backoff, idempotency, queues, resource
  limits, feature flags/gradual rollout switches, observability baselines, or
  when the user mentions reliability / runtime / health check / retry /
  timeout / worker / feature flag / 特性开关 / 稳定性.
  Detailed telemetry design defers to observability.
---

# Runtime Reliability

长期运行进程必须能启动、停止、降级、观测和恢复。纯库或一次性脚本按需裁剪。

更多运行时可靠性样例见 [examples.md](examples.md)。

## 审查顺序

1. 启动：配置是否完整，失败是否明确
2. 就绪：什么时候可以接流量/处理任务
3. 运行：超时、重试、背压、资源上限是否明确
4. 关闭：是否优雅停止、排空、释放资源
5. 观测：日志、指标、trace/request id 是否足够定位问题

## 健康检查

区分：

- **liveness**：进程是否应该继续活着；失败意味着可重启
- **readiness**：是否可以接流量/消费任务；失败意味着暂时摘流

规则：

1. readiness 检查关键依赖或内部队列状态，不要无脑返回 200
2. liveness 不应依赖所有外部服务，避免依赖抖动导致重启风暴
3. 探针语义写入文档或配置注释

## 优雅退出

1. 处理 `SIGTERM` / 平台等价信号
2. 停止接新请求/新任务
3. 给在途请求/任务有限时间完成
4. 刷日志、提交 offset、关闭连接池
5. 超时后硬退出并记录原因

避免重复注册信号处理或静默忽略退出信号。

## 超时、重试、退避

1. 所有外部调用必须有默认超时：HTTP、RPC、数据库、队列、文件锁
2. 重试只用于幂等或明确可安全重试的操作
3. 使用指数退避、抖动和最大次数/最大总时长
4. 不重试权限失败、校验失败、明显永久错误
5. 超时和重试参数集中配置，不散落魔法数字

## 幂等与去重

1. 至少一次投递的 worker 必须支持去重或幂等处理
2. 创建类 API/任务建议使用业务键或 idempotency key
3. 记录处理结果时要考虑并发重复提交
4. 幂等窗口、过期策略和冲突语义要写清

## 背压与资源上限

1. 队列长度、连接池、并发任务、缓存大小必须有上限
2. 达到上限时明确拒绝、排队、降级或丢弃策略
3. 禁止无界 goroutine/thread/task、无界 channel、无界缓存
4. 热路径避免不必要分配；复杂度变化需说明

## 可观测性

最小要求见下；更完整的日志/指标/追踪/SLO/告警规则 → `observability`。

日志：

- 使用结构化日志
- 关键事件包含 request_id / trace_id / job_id
- 不记录敏感原文

指标：

- 请求/任务数量、错误率、延迟
- 队列长度、重试次数、超时次数
- 资源使用：连接池、内存、线程/任务数

追踪：

- 跨服务传播 trace/request id
- 不依赖线程局部状态跨异步边界传上下文

## Worker / 队列

1. 消费端要定义 ack/nack 时机
2. 失败重试要有死信队列或人工处理路径
3. poison message 不应阻塞整个队列
4. 部署多个 worker 时考虑并发锁和重复执行

## 特性开关

用于灰度、紧急关闭与实验，不替代正确的迁移/发布流程。

1. 开关默认安全：失败时偏向关闭新路径或保持旧行为
2. 每个开关写清：控制范围、默认值、负责人、清理截止日期
3. 开关判断集中，避免散落魔法字符串；配置来源可审计
4. 评估顺序稳定：环境杀开关 > 租户/用户定向 > 百分比灰度
5. 观测：按开关状态打点/日志字段，便于对比与回滚
6. 长期开关视为技术债；上线完成后按期删除旧路径
7. 需要数据兼容时，先 `migration` expand，再靠开关切流，最后 contract

## 测试建议

- 关闭信号：确认停止接新任务并释放资源
- 超时：外部依赖卡住时能快速失败
- 重试：临时错误重试，永久错误不重试
- 幂等：重复消息/请求只产生一次业务效果
- 背压：队列满或并发满时行为明确
- 开关：开/关/灰度比例下的关键路径与回退

## 禁止

- 无超时外部调用
- 用无限重试掩盖失败
- 靠 `sleep` 处理竞态
- readiness/liveness 语义混淆
- 无界队列、无界缓存、无界任务
- 永久特性开关却从不删除旧实现
