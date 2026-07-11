---
name: api-design
description: >-
  Design and review APIs, including REST/HTTP, RPC, CLI-facing contracts,
  request/response schemas, error semantics, pagination, idempotency,
  versioning, compatibility, and OpenAPI/docs sync. Use when creating or
  changing endpoints, public interfaces, SDK contracts, webhooks, or when the
  user mentions API design / REST / OpenAPI / 接口设计.
---

# API Design

API 是长期契约。优先保持清晰、可演进、可测试、可文档化。
领域不变量与一致性边界 → `data-modeling`；schema/格式迁移步骤 → `migration`。

更多接口设计样例见 [examples.md](examples.md)。
参考资料见 [reference.md](reference.md)。


## 设计顺序

1. 明确消费者：前端、外部客户、内部服务、CLI、SDK
2. 明确资源/动作与成功路径
3. 设计错误语义、权限边界、幂等性和兼容性
4. 写示例请求/响应
5. 同步测试与文档（OpenAPI、README、SDK、迁移说明）

## HTTP / REST

1. 资源用名词：`/users/{id}`、`/orders/{id}/items`
2. 动作用方法表达：`GET` 查询、`POST` 创建/动作、`PATCH` 部分更新、`DELETE` 删除
3. 状态码表达协议层结果，不把所有错误都包成 `200`
4. 路径参数用于资源身份；查询参数用于过滤、分页、排序、展开字段
5. 批量或动作接口可用明确动作名：`POST /imports/{id}:dry-run`（按项目风格）

## 错误响应

错误响应应稳定、可机器处理、可定位：

```json
{
  "error": {
    "code": "invalid_request",
    "message": "Human-readable summary",
    "details": [],
    "request_id": "..."
  }
}
```

- `code` 稳定，给程序判断
- `message` 给人读，不承诺精确匹配
- `details` 放字段级错误或约束失败
- 不泄露栈、SQL、绝对路径、密钥、内部拓扑

## 分页 / 过滤 / 排序

1. 新接口优先 cursor pagination；简单内部列表可用 offset，但要说明限制
2. 返回是否还有下一页：`next_cursor` / `has_more`
3. 排序字段必须 allowlist；默认排序稳定
4. 过滤参数要有类型、范围和组合规则
5. 大列表必须有默认 limit 和最大 limit

## 幂等性

1. 创建/支付/导入/消息投递等非幂等操作应支持 idempotency key 或业务去重键
2. 重试安全性必须写入 API 文档
3. 服务端保存幂等结果时要定义过期窗口
4. 客户端可重试的错误要明确

## 兼容性与版本

1. 新增可选字段通常兼容；删除/重命名/改类型/改语义通常破坏兼容
2. 响应新增字段时客户端不得依赖字段顺序
3. 破坏性变更必须有版本策略、迁移说明、CHANGELOG
4. API 版本放路径、header 或媒体类型时，跟项目既有风格一致
5. 序列化格式和错误 `code` 视为契约，不能随意改

## 权限与安全

1. 每个接口明确认证要求和授权规则
2. 多租户接口必须按 tenant/org/owner 隔离查询
3. 不信任客户端传来的 owner、role、price、status 等敏感字段
4. 输入校验在边界层执行；内部函数可假设已通过校验
5. 详细安全规则见 `secure-coding`

## 文档与测试

1. 新/改接口同步 OpenAPI 或等价 API 文档
2. 文档至少包含：认证、参数、请求示例、响应示例、错误示例、分页/幂等规则
3. 测试覆盖成功、权限失败、校验失败、边界、兼容性关键路径
4. SDK/CLI 暴露的接口变化同步示例和迁移说明

## 禁止

- 所有错误返回 `200`
- 未定义错误格式就散落字符串错误
- 分页无上限
- 动态排序/字段选择未做 allowlist
- 破坏兼容但不更新文档、CHANGELOG 或迁移说明
