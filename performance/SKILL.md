---
name: performance
description: >-
  Improve and review software performance with measurement-first discipline:
  define budgets, benchmark, profile, fix hotspots, and guard against
  regressions. Use when optimizing latency/throughput/memory/CPU, investigating
  slowness, adding benchmarks, or when the user mentions performance /
  profiling / benchmark / 性能 / 优化 / 变慢.
  Correctness and reliability defer to testing, debugging, and
  runtime-reliability.
---

# Performance

先证明慢在哪里，再改。没有测量的优化默认视为投机。

落地样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 审查顺序

1. **目标**：慢在哪条路径、对谁可见、可接受预算是什么
2. **复现**：稳定复现或代表性负载
3. **测量**：端到端延迟/吞吐 + 剖析定位热点
4. **改动**：最小改动消除主导成本
5. **防护**：基准或回归门禁，防止回潮

## 性能预算

1. 先写清预算：p95 延迟、吞吐、内存上限、启动时间、包体积等
2. 区分冷启动与稳态、本地与生产近似环境
3. 优化目标必须可验证；「感觉更快」不够
4. 多目标冲突时明确优先级（通常正确性 > 可维护性 > 性能，除非项目另有约束）

## 测量方法

1. 先看端到端，再下钻：请求/任务总耗时 → 依赖等待 → CPU/分配/锁
2. 使用项目既有工具：基准测试、profiler、火焰图、tracing、`perf` 等
3. 对比要控制变量：同一数据规模、同一并发、同一构建类型（release/opt）
4. 记录基线数字；改完后用同一方法复测
5. 警惕噪声：预热、缓存、GC、CPU 变频、共享机器干扰

## 常见热点类别

优先检查：

- 多余 I/O、N+1 查询、重复序列化
- 无界或过大的内存拷贝/分配
- 锁竞争、过度同步、伪共享
- 算法复杂度从近似线性恶化到平方/更高
- 热路径日志、反射、正则编译、重复解析
- 同步阻塞放在本可并发/异步的路径上

## 优化规则

1. 只优化测量证明过的热点；一次改一个主导因素
2. 保持行为不变，除非用户明确接受语义变化换性能
3. 缓存必须有：键、失效、内存上限、穿透/击穿策略
4. 并发优化先保证正确；数据竞争不是性能特性
5. 可读性明显受损时，用注释写清「为什么快、测量证据、限制条件」

## 基准与回归

1. 关键路径应有可重复基准或性能回归测试
2. 基准名字说明场景与规模；断言写预算，不只打印数字
3. CI 中的性能门禁要稳定；抖动大时用相对阈值 + 重试/中位数，而不是关掉检查
4. 大优化附带前后数据：环境、命令、结果摘要

## 与其他 skill 的边界

- 正确性与回归测试 → `testing`
- 故障复现与假设收敛 → `debugging`
- 超时、队列、背压 → `runtime-reliability`
- 指标/追踪是否足够观察性能 → `observability`

## 禁止

- 无基线、无复测的「全面优化」
- 为微基准胜利牺牲 API 清晰度或正确性
- 过早引入复杂缓存/无界缓冲
- 在 Debug/未优化构建上做最终结论
- 用扩大超时掩盖真实变慢
