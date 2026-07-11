---
name: ci-quality
description: >-
  Design and review CI quality gates, local hooks, and repository checks for
  software projects. Use when setting up GitHub Actions/GitLab CI, pre-commit,
  format/lint/test/type-check workflows, dependency audits, coverage gates,
  or when the user mentions CI / pre-commit / quality gates / 持续集成.
---

# CI Quality

CI 与本地命令应使用同一套质量入口，避免「本地能过、CI 不过」或 Agent 猜命令。

## 最小门禁

1. 格式检查：只检查，不在 CI 自动改写
2. lint / 静态分析：警告视为失败
3. 构建 / 类型检查：确保可编译、可导入、可链接
4. 测试：覆盖变更路径；重要项目加入覆盖率门禁
5. 依赖 / 安全：面向生产或外部输入的项目加入依赖审计和密钥扫描

## 本地入口

项目应提供统一命令：

```bash
make check
make test
```

或等价 `just check`、`uv run ...`、`cargo ...`、`npm run ...`。CI 调用同一入口或其严格超集。

## pre-commit

适合放：

- 格式化或格式检查
- 快速 lint
- 拼写检查（docs/README/注释）
- 密钥扫描
- commit-msg 校验（若采用 Conventional Commits）

不适合放：

- 慢速 E2E
- 大覆盖率报告
- 长时间安全扫描
- 需要真实外部服务的检查

## 质量门限

按项目规模选择：

- 文件/函数复杂度上限
- 函数参数数量上限
- 覆盖率阈值
- 未使用依赖/死代码检查
- 文档链接检查
- 许可证和依赖漏洞检查

门限应优先增量收紧，不为历史债务一次性阻断所有开发。

## GitHub Actions 建议

1. PR 必跑：format、lint、build/type-check、test
2. main 定时或合并后跑：依赖审计、覆盖率上传、慢速 E2E
3. 使用缓存，但不要缓存会隐藏问题的构建产物
4. matrix 只覆盖真正支持的平台/版本，不做展示性膨胀

## 禁止

- CI 与 README/Makefile 中的命令不一致
- 为了让 CI 绿而跳过失败测试
- 在 CI 日志输出密钥或完整环境变量
- 把耗时很高的检查塞进每次提交前钩子
