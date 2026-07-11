---
name: testing
description: >-
  Design and improve tests for software changes, focusing on behavior, edge
  cases, regressions, and maintainable test structure. Use when writing tests,
  improving coverage, fixing flaky tests, or when the user mentions testing /
  test plan / pytest / cargo test / unit tests.
  Language-specific test tools defer to python-style, rust-style, cpp-style, etc.
---

# Testing

测试关注「用户可观察行为」与「未来回归是否会被抓住」。语言工具细节交给对应 `*-style`。

更多测试设计样例见 [examples.md](examples.md)。

## 先判断测试层级

| 变化 | 优先测试 |
|------|----------|
| 纯函数 / 小逻辑 | 单元测试 |
| 模块协作 / I/O 边界 | 集成测试 |
| 用户流程 / CLI / API | 端到端或黑盒测试 |
| 修 bug | 先写能复现 bug 的回归测试 |
| 重构无行为变化 | 依赖既有测试；必要时补缺口 |

## 测试设计

1. 测行为，不测实现细节；避免断言私有中间变量
2. 覆盖正常路径、边界、错误路径；不要只测 happy path
3. 一条测试一个主要意图；名字说明场景与期望
4. 测试数据最小但真实；避免巨大 fixture 掩盖重点
5. 时间、随机、网络、文件系统等不稳定依赖要隔离或固定

## 目录与数据

1. 集成测试优先放顶层 `tests/`；共享辅助放 `tests/common/` 或语言惯用位置
2. 测试数据放 `tests/fixtures/`，命名说明场景；不要依赖本机绝对路径
3. E2E 测试依赖外部服务时提供 mock、容器化环境或明确跳过条件
4. 特殊环境（裸机、硬件、外部 SaaS）要在文档里说明替代验证方式

## 断言

1. 断言要具体：值、状态、错误类型、日志/输出（确有必要时）
2. 错误路径测试应检查错误类别或关键信息，而不只检查「抛了」
3. 参数化用于同一行为的多个输入，不要把不同场景硬塞一起

## Flaky Test

处理顺序：

1. 确认是否与时间、并发、随机、外部服务、测试顺序有关
2. 固定种子/时钟；用临时目录；隔离全局状态
3. 删除隐式依赖测试顺序的共享状态
4. 不要简单增加 sleep；若必须等待，用条件等待和超时

## 覆盖率

1. 覆盖率是回归信号，不是目标本身；不为数字写空测试
2. 关键路径可设覆盖率门禁；门禁应在 CI 中执行，不必放入 pre-commit
3. 覆盖率下降要说明原因，生成代码/平台分支可合理排除
4. 修 bug 优先补能失败的回归测试，再看覆盖率数字

## Test Plan

提交或 PR 中写清：

```markdown
## Test plan
- [ ] 新增/更新的自动化测试
- [ ] 相关命令（如 pytest / cargo test / ctest）
- [ ] 手动验证路径（仅自动化不足时）
```

## 禁止

- 为了覆盖率写没有断言价值的测试
- 只 mock 自己写的全部逻辑，导致测试不验证真实行为
- 修 bug 但不补回归测试（除非说明无法自动化）
- 让测试依赖本机绝对路径、真实网络或执行顺序
