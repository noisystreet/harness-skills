---
name: code-review
description: >-
  Review code changes for correctness, regressions, maintainability, security,
  and test gaps. Use when reviewing pull requests, diffs, local changes, or when
  the user asks for code review / review / 审查 / 看看改动.
  Style-specific checks defer to clean-code and language *-style skills.
---

# Code Review

以发现真实问题为目标，不做泛泛风格点评。通用可读性见 `clean-code`，语言惯用法见对应 `*-style`。

更多输出样例见 [examples.md](examples.md)。

## 审查顺序

1. **正确性**：行为是否符合需求；边界、空值、错误路径、并发、状态转移是否正确
2. **回归风险**：是否破坏既有 API、数据格式、兼容性、性能或安全假设
3. **测试缺口**：新增/变更行为是否有测试；是否覆盖失败路径与边界
4. **文档与迁移**：API/架构/配置/用户行为变化是否更新 README、CHANGELOG、迁移说明
5. **可维护性**：是否有隐式状态、过大函数、重复逻辑、误导性命名
6. **安全**：输入校验、权限、注入、敏感信息、依赖风险

## 输出格式

有问题时， findings 放最前面，按严重度排序：

```markdown
## Findings
- [Severity] `path`: 问题描述；为什么会出错；建议修法

## Questions
- 需要确认的问题（没有则省略）

## Summary
简短概括改动与残余风险
```

没有问题时直接说「未发现阻塞问题」，并指出仍未验证的测试/运行风险。

## 严重度

- **Critical**：会导致数据丢失、安全漏洞、生产故障、无法编译/启动
- **High**：明显行为错误、重要回归、缺少关键错误处理
- **Medium**：边界缺陷、测试缺口、维护风险较高
- **Low**：小的可读性或一致性问题；不要淹没主要问题

## 规则

1. 优先报 bug 和风险；少报纯风格问题
2. 每条 finding 必须能定位到具体文件/代码区域，并说明影响
3. 不确定就写 question，不要臆断
4. 不重复报告同一根因；合并同类项
5. 不要求无关重构；建议应与本次改动范围相称

## PR 规模与协作

1. 单 PR 建议不超过约 400 行有效改动（不含测试、格式化、生成文件）；超出应拆分或要求作者说明
2. PR 描述应包含变更摘要、测试策略、影响范围；无法验证的部分必须标注风险
3. 文档、CHANGELOG、配置示例、迁移说明应随行为/API 变化同步
4. 格式问题交给 CI/format 工具；人工审查聚焦逻辑正确性、安全和边界
5. 非阻塞建议用 `nit:` 或明确标为建议，不阻断合并

## 禁止

- 用「看起来不错」代替审查
- 只复述改了什么，不指出风险
- 大量挑格式而忽略行为问题
- 要求引入与项目既有模式冲突的新框架/新抽象
