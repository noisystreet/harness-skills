# GitHub Flow — 参考

主路径见 [SKILL.md](SKILL.md)。此处为边界场景与日常 Git 卫生。

## 日常 Git 卫生

这些规则服务本地可预测性，减少脏工作区、错误分支和不可恢复的历史改写。

### 开工前

1. 先看状态：`git status -sb`；有未提交改动时不要盲目切分支
2. 从最新主干开分支：`git fetch origin && git checkout main && git pull --ff-only`
3. 一件事一条短分支；分支名用 `feat/` `fix/` `docs/` `chore/` `hotfix/` 等前缀
4. 不要在 `main` 上直接堆功能提交（仓库明确允许直推除外）

### 提交中

1. 小步、可审查；提交信息按 `commit-message`
2. 提交前跑项目质量入口（如 `make check`）；不要把明显红灯推进远端
3. 不提交密钥、`.env`、构建产物、本机绝对路径配置
4. 相关文件一起进同一逻辑提交；不要把无关格式化混进行为变更（除非用户要求大清理）

### 暂存与清理

| 场景 | 做法 |
|------|------|
| 临时打断，改动还不能提交 | `git stash push -u -m "wip: …"`，回来再 `stash pop` |
| 改动属于当前功能但未完成 | 优先 draft PR / WIP 提交，少用长期 stash |
| 误改文件想丢弃 | 确认无价值后 `git restore -- <path>`；已 staged 用 `git restore --staged` |
| 看不清自己改了什么 | `git diff` / `git diff --cached`；需要时再 `git log -p` |

### 更新与同步

1. 工作中定期 `git fetch origin`，避免一次性巨大 rebase
2. 功能分支跟上 `main`：优先 rebase；他人已基于你的分支则改 merge（见下方 Rebase vs merge）
3. PR 合入后删除本地/远端功能分支，切回 `main` 并 `pull --ff-only`
4. 发现本地 `main` 与远端分叉且内容等价（如签名重写提交）：以 `origin/main` 为准对齐，不要长期双轨

### 改写历史（高风险）

允许（需同时满足）：

- 仅改**本人**、未共享或短生命周期分支
- 目的明确：修补刚提交的笔误、rebase 到最新 `main`、整理未审查的本地提交

默认禁止：

- 改写已合入 `main` 的历史
- 在他人正在基于的分支上 `rebase` / `commit --amend` / force push 而不协调
- 用 `reset --hard` 丢弃有价值的未备份工作
- 用 `--force` 代替 `--force-with-lease`

`commit --amend` 额外条件：

1. 只改 HEAD，且该提交通常尚未推送；或推送后仅本人分支并随后 `--force-with-lease`
2. 不把无关新文件偷偷塞进「旧」提交来掩盖审查范围
3. 用户规则/仓库钩子禁止 amend 时，改为新提交

### 排查与恢复

1. 找引入点：`git bisect`（配合测试命令）；范围要可复现
2. 误删分支/提交：先 `git reflog`，再恢复；不要立刻 `gc` / 硬清理
3. 冲突解决不了或不懂业务语义：停下询问，不要猜

### 配置与忽略

1. 不把本机 `user.name` / `user.email` / 签名配置写进仓库文档当「项目要求」的唯一真值
2. 本地忽略用 `.git/info/exclude` 或个人 global ignore；共享规则进 `.gitignore`
3. 大文件、生成物、环境文件进 ignore；发现误提交先停推送并按仓库流程处理（必要时轮换密钥）

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

## 外部参考

### Guides

- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) - 官方短生命周期分支与 PR 流程
- [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) - PR 协作模型
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) - 保护 `main`、要求 CI/review
- [Pro Git book](https://git-scm.com/book/en/v2) - 分支、rebase、reflog 等底层概念
- 本仓库 `commit-message` - 提交信息规范
- 本仓库 `release` - tag、CHANGELOG、发版与回滚

### What To Learn

- 主干始终可发布；功能在短分支上通过 PR 进入
- 用保护规则与 CI 防止直推破坏 `main`
- 改写历史只限于本人短分支，并优先 `--force-with-lease`
- 日常保持干净工作区：先 `status`，再切分支 / rebase / 发 PR

### Caveats

- 组织可能强制 squash merge 或 merge commit；以仓库设置为准
- Pro Git 覆盖面广，按需查阅，不要把全书规则一次性塞进每个 PR
- 提交信息与发版细节以 `commit-message` / `release` 为准，本文件不重复展开
