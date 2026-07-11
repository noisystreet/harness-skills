---
name: debugging
description: >-
  Debug software failures systematically by reproducing, gathering evidence,
  narrowing hypotheses, and verifying fixes. Use when investigating bugs,
  failing tests, crashes, performance anomalies, flaky behavior, or when the
  user mentions debug / debugging / 排查 / 报错 / 失败.
---

# Debugging

先证据，后修改。每次只验证一个假设，避免边猜边改。

更多排障报告样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 流程

1. **复现**：拿到最小命令、输入、环境、期望与实际结果
2. **观察**：读错误栈、日志、测试输出、最近改动；不要只看最后一行
3. **缩小范围**：二分输入、配置、提交、模块；找第一个坏点
4. **提出假设**：写清「如果 X 是原因，应看到 Y」
5. **验证假设**：加最小日志/断言/临时测试；一次只改一个变量
6. **修复**：改最小必要代码，保留设计边界
7. **防回归**：补测试或说明无法自动化

## 优先证据

- 完整错误信息与调用栈
- 能稳定复现的最小用例
- 失败前后的输入/状态差异
- 最近变更、依赖版本、配置变化
- 并发/时间/随机/缓存/环境变量等非确定因素

## 常见方向

| 症状 | 先查 |
|------|------|
| 本地过 CI 失败 | 环境、路径、时区、依赖版本、并发顺序 |
| 偶现失败 | 竞态、时间、随机、共享状态、测试顺序 |
| 行为突然变慢 | 数据规模、循环/查询次数、缓存失效、I/O |
| 线上才失败 | 配置、权限、数据形态、外部服务契约 |
| 修一个坏另一个 | 隐式状态、全局状态、边界条件没建模 |

## 修改原则

1. 先写/保留复现用例，再改代码
2. 修根因，不只吞异常或加 fallback 掩盖
3. 临时日志、调试 print、实验代码要清理
4. 修完跑相关测试；无法跑要说明原因与风险

## 汇报格式

```markdown
## Root cause
一句话说明根因

## Evidence
- 支撑证据

## Fix
- 改了什么，为什么能解决

## Verification
- 跑过的测试/命令，或未跑原因
```

## 禁止

- 未复现就大改
- 同时改多个无关假设
- 靠 sleep 掩盖竞态
- 吞掉错误让失败「消失」
