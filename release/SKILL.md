---
name: release
description: >-
  Plan software releases with versioning, changelog cutover, tags, rollout,
  verification, and rollback. Use when cutting a version, publishing GitHub
  Releases, doing canary/staged rollouts, writing release notes, or when the
  user mentions release / versioning / tag / rollback / canary / 发版 / 回滚 /
  发布。
  Migration expand/contract details defer to migration; CI gates defer to
  ci-quality.
---

# Release

发布是可回滚的变更交付，不是「合并到 main」的同义词。默认小步、可观察、可撤销。

落地样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 审查顺序

1. **发布内容**：包含哪些用户可见变化与风险
2. **版本与说明**：版本号、CHANGELOG、迁移/破坏性提示
3. **门禁**：测试/检查是否已绿，产物是否可复现
4. ** rollout**：全量还是灰度，观察信号是什么
5. **回滚**：谁执行、怎么执行、数据是否可回

## 版本与 CHANGELOG

1. 采用项目已有版本策略；无策略时用语义化版本：
   - `MAJOR`：破坏性变更
   - `MINOR`：兼容新功能
   - `PATCH`：兼容修复
2. 发版前把 `[Unreleased]` 切到新版本分区，并开新的 `[Unreleased]`
3. 破坏性变更、安全修复、迁移步骤必须出现在说明里
4. tag 与版本号一致（如 `v0.1.0`），避免「文档一个版本、tag 另一个」

## 发布清单

发版前：

1. `main`（或发布分支）包含目标提交
2. CI 绿：`check` / test / 必要审计
3. CHANGELOG 与文档已更新
4. 迁移/配置变更有执行顺序（见 `migration`）
5. 明确是否需要特性开关或灰度

发版中：

1. 打 tag / 生成 GitHub Release（如适用）
2. 发布产物或触发部署
3. 观察错误率、延迟、关键业务指标、日志/告警

对本仓库（Harness Skills）：用 `make release VERSION=x.y.z`，再 `git push origin HEAD && git push origin vx.y.z`；GitHub Actions 会用 CHANGELOG 对应段落创建 Release。

发版后：

1. 验证冒烟路径
2. 公告/Release notes 对受众可见
3. 打开下一版本 `[Unreleased]` 收集体检

## 灰度与 Canary

1. 先小流量或单区域，再扩大
2. 观察窗口与成功/失败标准预先写清
3. 失败默认回滚或暂停扩大，不「再等等看」而无期限
4. 配置/数据迁移与代码发布的顺序写进清单，避免新代码读不到新列

## 回滚

1. 每个发布都有默认回滚路径：重新部署上一版本、关开关、切回旧读路径等
2. 区分：
   - **代码回滚**是否足够
   - **数据/迁移**是否需要补偿（常不可简单回滚）
3. 回滚决策阈值：错误率、SLO burn、关键路径失败
4. 回滚后保留时间线：何时发布、观察到什么、何时回滚

## 产物与可复现

1. 发布产物应可从 tag 重建（锁文件、构建命令、镜像 digest）
2. 不要用手改生产热修却无提交/tag
3. 密钥与环境差异不进产物；用运行时配置注入

## 与其他 skill 的边界

- 质量门禁 → `ci-quality`
- schema/API 迁移步骤 → `migration`
- 特性开关切流 → `runtime-reliability`
- Release notes 文风 → `docs-style`
- 依赖供应链 → `dependency-management`

## 禁止

- 无 CHANGELOG/无 tag 的「静默发版」
- 破坏性变更不公告
- 不可回滚却当常规发布强推
- 用扩大超时/关告警代替回滚决策
- 把本地未推送提交当成已发布版本
