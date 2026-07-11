---
name: commit-message
description: >-
  Generate and review clear Conventional Commit messages from git diffs,
  staged changes, or change descriptions. Use when writing commits, reviewing
  commit history, choosing feat/fix/refactor/chore/test/docs types, or when the
  user mentions commit message / 提交信息 / 写提交.
---

# Commit Message

提交信息说明「为什么这次改动存在」，而不是复述文件名。默认使用 Conventional Commits。

更多输入/输出样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 格式

```text
<type>(<scope>): <summary>

<body>
```

- `summary`：一句话，使用祈使/动词开头，简短明确
- `body`：可选；用于解释动机、行为变化、兼容性影响
- 多个无关改动应拆提交，不要写成一个大杂烩 commit

## Type 选择

| Type | 何时使用 |
|------|----------|
| `feat` | 新增用户可见能力或公开行为 |
| `fix` | 修复 bug、回归、错误行为 |
| `refactor` | 不改变外部行为的结构调整 |
| `perf` | 性能优化且行为不变 |
| `test` | 添加或调整测试 |
| `docs` | 文档改动 |
| `style` | 仅格式/排版，不影响行为 |
| `chore` | 构建、依赖、配置、维护杂项 |
| `ci` | CI/CD 配置 |
| `revert` | 回滚提交 |

不确定时优先按用户可见行为判断：有新能力用 `feat`，修错用 `fix`，只是内部整理用 `refactor`。

## Scope

- scope 可选；用模块、包、领域名，如 `auth`、`api`、`cli`、`deps`
- 不知道合适 scope 时省略，不要硬造
- 同仓库已有风格优先

## Summary

1. 写具体行为：`fix(api): handle empty token`，不要 `fix bug`
2. 不写句号结尾
3. 不塞太多细节；细节放 body
4. 避免「update files」「misc changes」「wip」

## Body

需要 body 的情况：

- 解释为什么这样修，而不是只说改了什么
- 行为变化、迁移步骤、兼容性影响
- 修复复杂 bug 的 root cause

模板：

```text
<type>(<scope>): <summary>

Explain why the change is needed and any important behavior change.
Mention tests or follow-up only when relevant.
```

## Breaking Change

破坏兼容时使用 `!` 或 footer：

```text
feat(api)!: require explicit tenant id

BREAKING CHANGE: callers must pass tenant_id when creating sessions.
```

## 生成流程

1. 先看 staged diff；只为将要提交的内容写消息
2. 判断主语义：新增、修复、重构、测试、文档、维护
3. 若 staged 内容包含多个无关主题，建议拆提交
4. 生成 1 个推荐消息；必要时给 2-3 个备选 type

## 快速示例

```text
feat(cli): add dry-run flag for imports
```

```text
fix(auth): reject expired refresh tokens

Validate the token expiry before rotating credentials so stale sessions cannot
receive a new access token.
```

```text
refactor(parser): replace boolean flags with parse state
```

## 禁止

- `wip`、`misc`、`update`、`changes` 作为最终提交信息
- 为未 staged 的改动写进提交消息
- 把多个无关改动包装成一个笼统 commit
- 在消息里泄露密钥、内部 URL、个人敏感信息
