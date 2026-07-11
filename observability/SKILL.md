---
name: observability
description: >-
  Design and review observability for applications and services: structured
  logs, metrics, traces, correlation IDs, SLIs/SLOs, and actionable alerts.
  Use when adding logging/metrics/tracing, debugging production with telemetry,
  defining dashboards/alerts, or when the user mentions observability /
  OpenTelemetry / metrics / tracing / SLO / 可观测 / 监控告警.
  Runtime failure modes defer to runtime-reliability; secret redaction defers
  to secure-coding.
---

# Observability

目标是能在生产中快速回答：发生了什么、影响谁、严重到什么程度、下一步查哪里。
优先有用信号，不堆无标签指标。

落地样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 审查顺序

1. **关联**：请求/任务是否有稳定 correlation id，并跨边界传播
2. **日志**：是否结构化、分级正确、含关键字段、已脱敏
3. **指标**：是否覆盖流量、错误、延迟、饱和度（RED/USE）
4. **追踪**：关键路径是否可串联；采样策略是否合理
5. **告警**：是否对应用户影响或 SLO，而不是原始噪声

## 关联与上下文

1. 每个请求/任务至少有一个 `request_id` / `trace_id` / `job_id`
2. 跨服务、队列、异步任务必须显式传递上下文，不依赖线程局部碰运气
3. 日志、指标标签、trace span 使用同一套标识字段名
4. 用户/租户 id 可记录时要评估隐私与泄露风险

## 日志

1. 使用结构化日志（JSON 或等价键值），避免只能靠正则解析的自由文本
2. 事件写「发生了什么 + 关键维度」，不写大段调试散文
3. 级别：`error` 需人处理；`warn` 可恢复异常；`info` 关键业务节点；`debug` 默认关闭
4. 禁止记录密钥、token、密码、完整支付信息、未必要的 PII
5. 错误日志保留足够上下文（操作、资源 id、错误类别），不要只打 `failed`

## 指标

最少覆盖：

- **Rate**：请求/任务吞吐
- **Errors**：错误率或失败计数（按类型分类）
- **Duration**：延迟分布（p50/p95/p99 或直方图）
- **Saturation**：队列深度、连接池使用率、线程/worker 占用

规则：

1. 指标名稳定、单位明确；标签基数受控（禁止高基数 user_id/email 当标签）
2. 区分用户错误与系统错误，避免把 4xx 全算成服务故障
3. 关键依赖调用单独计量（超时、重试、上游错误）
4. 仪表盘先服务排障，不先做好看的大屏

## 追踪

1. 入口、出站调用、队列生产/消费、重要内部阶段打 span
2. span 名称表达业务操作，不堆无意义的函数名
3. 属性记录稳定维度；大 payload 不进 span
4. 采样策略写清：错误/慢请求可提高保留率
5. 没有分布式追踪时，至少保证日志关联 id 可串联

## SLO 与告警

1. SLI 应对齐用户体验：可用性、成功延迟、新鲜度等
2. 告警优先「正在伤用户」或「快违反 SLO」，少告「某计数器上涨」
3. 每条告警要有：含义、影响、初始排查步骤、负责人/路由
4. 可自动恢复的抖动用抑制/窗口，避免夜惊
5. 无 runbook 的告警视为未完成

## 与其他 skill 的边界

- 超时/重试/背压/优雅退出 → `runtime-reliability`
- 密钥脱敏与安全事件 → `secure-coding`
- 性能剖析与基准 → `performance`
- 故障定位流程 → `debugging`

## 禁止

- 用 `print` / `println` 充当生产日志
- 高基数标签撑爆时序库
- 告警风暴却没有降噪和归属
- 记录敏感原文「方便排查」
- 只加观测、不验证能否据此定位一次真实故障
