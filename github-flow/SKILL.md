---
name: github-flow
description: >-
  Follow GitHub Flow for branching, commits, PRs, review, and merge.
  Use when creating branches, opening or updating pull requests, handling
  review comments, merging, resolving conflicts, or when the user mentions
  GitHub Flow / PR / MR / 开 PR / 提 PR / 合并分支 / 分支流程.
---

# GitHub Flow

主干始终可发布。短生命周期功能分支 → PR → review → 合并回 `main`。

边界场景（rebase、冲突、draft、force-with-lease）见 [reference.md](reference.md)。

## 决策速查

| 情况 | 做法 |
|------|------|
| 改动未就绪 / 要早讨论 | 开 **draft PR** |
| 常规功能或文档 | 就绪后开正式 PR，选 `templates/pr-feature.md` |
| 修 bug | `templates/pr-bugfix.md` |
| 线上紧急修复 | 从 `main` 开 `hotfix/…`，用 `templates/pr-hotfix.md`；仍走 PR，除非用户明确接受风险 |
| 合并方式 | 默认 **rebase merge**（保留逐条 commit）；仓库另有约定则跟仓库 |
| 改写已推送历史 | 仅本人短分支，用 `--force-with-lease`；见 reference |
| PR 过大（难审） | 拆成多个 PR，不要硬推 |

## 主路径清单

按顺序执行；用户规则里已有更细的 git/PR 约束时，以用户规则为准，本 skill 补流程缺口。

### 1. 分支

```bash
git checkout main && git pull
git checkout -b <type>/<short-desc>
```

- 前缀：`feat/` `fix/` `docs/` `refactor/` `chore/` `hotfix/`
- 一件事一条分支；生命周期尽量短（天级）
- 禁止直推 `main`（除非用户明确要求）

### 2. 提交与推送

1. 小步、可审查；提交信息按 `commit-message` skill，消息写「为什么」而不是文件清单
2. 首次：`git push -u origin HEAD`；之后：`git push`

### 3. 开 PR

```bash
gh pr create --title "<title>" --body "$(cat <<'EOF'
<粘贴对应 templates/pr-*.md 填好的正文>
EOF
)"
```

- 目标分支：`main`（或仓库默认主干）
- 按类型读模板并填写：
  - 功能 / 重构 / 文档 → [templates/pr-feature.md](templates/pr-feature.md)
  - Bug → [templates/pr-bugfix.md](templates/pr-bugfix.md)
  - 紧急修复 → [templates/pr-hotfix.md](templates/pr-hotfix.md)
- 未就绪：`gh pr create --draft …`
- CI 绿、无冲突后再请求 review / 合并；CI 门禁见 `ci-quality`
- 行为/API/配置变化时同步 README、CHANGELOG、迁移说明或 PR 中解释无需更新

### 4. Review

1. Critical 必须改；Suggestion 按判断采纳
2. 改完推送；需要时回复评论或 `@` reviewer
3. 不同意则简短说明理由，不沉默忽略

### 分支保护建议

- 默认分支禁止直推
- 合并前要求 CI 必过和至少一次 review（公开/团队项目）
- 按需启用线性历史，默认配合 rebase merge
- 禁止对默认分支 force-push

### 5. 合并与收尾

```bash
gh pr merge --rebase --delete-branch
git checkout main && git pull
```

- 默认 rebase：把 PR 上每条 commit 依次接到 `main`，不合成一团
- 合并前确认提交历史可上主干（小步、消息清楚）；若全是 WIP 垃圾提交，先在本分支整理再合，或经用户同意改用 squash
- 若仓库禁用 rebase merge，改用仓库默认
- 合并后确认本地 `main` 已更新

## 禁止

- 未经确认对共享分支 force push（`--force` 无 lease 更禁止）
- 无关改动塞进同一 PR
- 跳过 CI / review（hotfix 也需用户明确接受风险才可例外）
- 把本 skill 与用户 git 安全规则对着干（不 amend 他人提交、不改 git config 等）
