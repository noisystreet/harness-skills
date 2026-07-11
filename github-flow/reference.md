# GitHub Flow — 参考

主路径见 [SKILL.md](SKILL.md)。此处仅边界场景。

## Draft PR

- 适用：实现中、要设计讨论、CI 先跑起来、避免过早求 review
- 开：`gh pr create --draft …`
- 就绪：`gh pr ready`

## Rebase vs merge

| 目标 | 做法 |
|------|------|
| 更新功能分支以跟上 `main` | 优先 `git fetch origin && git rebase origin/main` |
| 已有人基于你的分支继续开发 | 不要 rebase；`git merge origin/main` |
| `main` 上的历史 | 不 rebase 公共 `main` |

Rebase 后若分支已推送：

```bash
git push --force-with-lease
```

禁止省略 lease 的 `git push --force`，除非用户明确要求且理解风险。

## 冲突处理

1. `git fetch origin`
2. `git rebase origin/main`（或 `git merge origin/main`，见上表）
3. 解决冲突 → `git add` → `git rebase --continue`（merge 则 commit）
4. 跑相关测试 / 确认编译
5. 推送（rebase 后用 `--force-with-lease`）

解决不了或冲突面过大：停下来问用户，不要猜测业务语义。

## force-with-lease

允许（需同时满足）：

- 分支为本人短生命周期功能分支
- 目的是 rebase / 整理提交后更新远端
- 用户未禁止 force push

不允许：

- `main` / 发布分支
- 他人正在基于该分支工作（改用新提交或先协调）
- 用 `--force` 代替 `--force-with-lease`

## Stacked / 依赖 PR

- 下游 PR 的 base 设为上游分支，不直接打到 `main`（除非工具链另有约定）
- 合并顺序：先上游，再下游；上游合并后把下游 retarget 到 `main` 并 rebase
- 每个 PR 仍须可独立理解与审查

## 合并方式例外

- 默认 **rebase merge**（见 SKILL）：保留逐条 commit，不 squash 成一团
- 仓库要求 merge commit 或 squash：跟仓库设置 / CONTRIBUTING
- 分支上尽是临时/WIP 提交且不愿整理：经用户同意可用 squash
- 需要显式合并节点（如发布汇合）：merge commit，并在 PR 说明原因

## Hotfix 例外

- 仍优先走 PR + CI
- 仅当用户明确说跳过 review/CI 并接受风险时，才直推或简化流程
- 事后用 Follow-up 项补测试与清理
