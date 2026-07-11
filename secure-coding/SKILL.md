---
name: secure-coding
description: >-
  Apply practical secure coding checks for application code, scripts, APIs,
  services, and automation. Use when writing or reviewing code that handles
  user input, authentication, authorization, secrets, files, shell commands,
  SQL/queries, network calls, logs, dependencies, or when the user mentions
  security / secure coding / 安全 / 漏洞 / 密钥.
---

# Secure Coding

默认假设输入不可信、权限需显式、密钥不可见。优先发现真实风险，不做安全八股。

## 审查顺序

1. **密钥与敏感信息**：是否进入代码、日志、错误、测试数据、提交历史
2. **输入边界**：外部输入是否校验、规范化、限制大小和类型
3. **权限**：是否在服务端/可信边界检查身份与授权
4. **注入风险**：SQL、命令、路径、模板、HTML、正则、反序列化
5. **数据暴露**：响应、日志、指标、异常信息是否泄露内部细节
6. **依赖与供应链**：新增依赖是否必要、可信、维护良好

## 密钥

1. 禁止把 token、密码、私钥、cookie、连接串写进仓库
2. 配置从环境变量、密钥管理器或部署平台注入
3. 日志与错误信息必须脱敏；不要打印完整 Authorization、Cookie、API key
4. 示例值使用明显假的占位符：`example-token`、`changeme`，不要像真实密钥
5. 发现疑似真实密钥：停止扩散，提醒用户轮换；不要在回复中复述完整密钥

## 仓库安全基线

1. 公开或多人协作项目应有 `SECURITY.md`，说明漏洞上报渠道；不要要求用户在公开 Issue 报漏洞
2. 提供 `.env.example`，并确保 `.env`、私钥、证书、真实配置进入 `.gitignore`
3. CI 或 pre-commit 可加入密钥扫描（如 gitleaks/trufflehog 同类工具），但注意误报和耗时
4. PR 模板应提醒检查敏感信息、权限逻辑和依赖风险

## 输入与验证

1. 所有外部输入都在边界校验：HTTP、CLI、文件、环境变量、队列消息、Webhook
2. 使用 allowlist 优先于 denylist
3. 明确长度、类型、范围、编码、文件大小、超时
4. 校验和规范化顺序要清楚（如路径、URL、大小写、Unicode）
5. 不信任客户端传来的角色、价格、owner_id、权限字段

## 认证与授权

1. 认证说明「是谁」，授权说明「能做什么」；两者都要检查
2. 权限检查放在服务端或可信边界，不依赖前端隐藏按钮
3. 多租户必须按 tenant / org / owner 隔离查询
4. 默认拒绝；新增入口要显式考虑权限
5. 安全失败返回信息要克制，不泄露用户是否存在、资源是否存在（按业务需要权衡）

## 注入风险

### SQL / 查询

- 使用参数化查询或 ORM 安全 API
- 禁止字符串拼接 SQL / filter / query DSL
- 动态排序/字段名只能来自 allowlist

### Shell 命令

- 优先不用 shell；用参数数组形式执行命令
- 需要 shell 时，对输入做 allowlist；不要拼接未信任字符串
- 设置超时、工作目录、环境变量白名单；避免继承敏感环境

### 路径与文件

- 防路径穿越：规范化后确认仍在允许目录内
- 不用用户输入直接组成文件路径或下载 URL
- 上传文件检查大小、类型、扩展名与内容；不要信任文件名

### Web 输出

- HTML/模板默认转义；需要原始 HTML 时必须说明可信来源
- JSON/API 不返回内部栈、SQL、绝对路径、密钥片段
- 设置合理的 CORS，不用 `*` 搭配凭证

## 反序列化与解析

1. 不反序列化不可信的 pickle、yaml unsafe loader、语言原生对象流
2. JSON/XML/YAML 解析限制大小和深度
3. XML 注意 XXE；用安全 parser 或禁用外部实体

## 依赖

1. 新增依赖必须有明确价值；小功能优先标准库
2. 检查维护状态、许可证、下载源、传递依赖风险
3. 固定或锁定版本按项目工具链执行
4. 不从随机脚本 URL 直接执行安装命令，除非用户明确接受风险

## 日志与错误

1. 日志记录事件和关联 id，不记录敏感原文
2. 错误对用户友好，对内部诊断留足上下文但不泄露秘密
3. 安全事件可记录谁、何时、资源、动作、结果；避免记录完整请求体

## 测试建议

- 权限：无登录、错误用户、跨租户、低权限角色
- 输入：空、超长、非法编码、特殊字符、路径穿越
- 注入：SQL 元字符、shell 元字符、HTML/JS payload
- 日志：确认敏感字段未出现

## 禁止

- 把安全风险用 TODO 留给以后，除非用户明确接受并记录风险
- 为了通过测试关闭鉴权/校验
- 捕获安全错误后静默放行
- 在回复、提交信息、日志中复述完整密钥或敏感数据
