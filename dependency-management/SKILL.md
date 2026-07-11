---
name: dependency-management
description: >-
  Choose, pin, audit, upgrade, and remove software dependencies with supply-chain
  awareness. Use when adding libraries, updating lockfiles, reviewing dependency
  diffs, evaluating licenses/advisories, or when the user mentions dependencies /
  lockfile / supply chain / cargo deny / npm audit / 依赖 / 升级依赖.
  Security review of app code defers to secure-coding; CI wiring defers to
  ci-quality.
---

# Dependency Management

依赖是生产代码的一部分。默认偏好标准库与已有依赖；新增必须有明确收益。

落地样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 审查顺序

1. **必要吗**：能否用标准库或现有依赖解决
2. **可信吗**：维护状态、来源、许可证、传递依赖体积
3. **可锁定吗**：版本策略与锁文件是否正确
4. **可升级吗**：有没有审计、变更说明和回滚路径
5. **可删除吗**：是否留下未使用依赖或死传递链

## 新增依赖

1. 写清引入理由：替代了什么、带来什么能力
2. 检查：最近提交、issue 响应、下载源、已知漏洞、许可证兼容
3. 评估传递依赖数量与体积；优先 API 面小、依赖少的库
4. 能用官方/生态主流实现就不要随便引入小众替代
5. 重要选型可用一页 ADR 记录取舍

## 版本与锁文件

1. 应用 / 可部署服务：提交锁文件，CI 按锁文件构建
2. 库 crate/package：按生态惯例决定是否锁；至少在 CI 测支持范围
3. 区分直接依赖与开发依赖；测试/lint 工具不要混进运行时依赖
4. 版本约束避免无上界的漂；也不要无理由钉死无法安全补丁升级
5. 变更锁文件时，PR 说明主要升级了什么、为何需要

## 升级与审计

1. 常规安全补丁优先；破坏性大版本单独升级并看 changelog
2. 升级后跑项目标准检查：`make check` / test / lint / 类型检查
3. 使用生态审计工具（如 `cargo deny`、`npm audit`、`pip-audit`、OSV）并处理真实风险
4. 忽略告警必须写理由与跟踪项；禁止盲加 exclude
5. 批量 Dependabot/Renovate PR 要按风险分组，不「全绿就盲合」

## 供应链卫生

1. 不从未知脚本 URL 直接 `| sh` 安装，除非用户明确接受风险
2. 固定 Git 依赖到 commit/tag，并说明原因
3. 私有源/镜像配置不把凭证写入仓库
4. 移除依赖后确认导入、文档和镜像层不再引用
5. 关注弃用公告与替换路径，避免拖到强制不可用

## 审查依赖 diff

关注：

- 新直接依赖及其传递闭包
- 许可证从宽松变为 copyleft 或不兼容
- postinstall/build script 是否执行网络或写盘
- 权限扩大：文件系统、网络、原生代码
- 替换包名是否可疑（typosquat）

## 与其他 skill 的边界

- 密钥与输入安全 → `secure-coding`
- CI 审计门禁接线 → `ci-quality`
- 语言工具链默认选择 → 对应 `*-style` / `project-bootstrap`
- 行为回归验证 → `testing`

## 禁止

- 「顺手」加入大型框架解决小问题
- 提交未审查的锁文件巨变
- 为消告警而关闭审计或钉死已知漏洞版本
- 把私有 token 写进依赖配置
- 复制粘贴来路不明的安装脚本进 README/CI
