---
name: rust-style
description: >-
  Apply Rust idioms and coding standards for idiomatic, safe, maintainable code.
  Use when writing, refactoring, or reviewing Rust code, Cargo projects, or when
  the user mentions Rust style / idioms / clippy / rustfmt / nextest / cargo deny.
  General readability rules defer to clean-code; this skill owns Rust-specific rules.
---

# Rust 编程规范

以可读、可维护、惯用 Rust 为准。默认遵循 `rustfmt` + `clippy`；新项目强烈推荐 `nextest`、`cargo deny`、`cargo machete`、`taplo`。
**命名意图、隐式状态、函数拆分等通用规则** → 见 `clean-code`。本文件只定 Rust 特例。
优秀项目、教材和官方资料 → 见 [reference.md](reference.md)。

## 硬规则（默认）

项目另有约定时跟项目；否则按此执行：

1. **库 crate**：错误用 `thiserror`（或等价类型化错误）；**禁止**把 `anyhow::Error` 放进公开 API
2. **应用 / binary**：可用 `anyhow` / `eyre`；边界处再映射
3. 非测试代码避免 `unwrap`；`expect` 必须写明不变量
4. 公开 API 输入优先借用（`&str`、`&[T]`、`impl AsRef<Path>`），不强收 `String`/`PathBuf`
5. 互斥状态用 `enum`，不用多布尔字段组合
6. 每个 `unsafe` 块上方用注释写清安全不变量；块外逻辑保持 safe
7. 改动后必须 `cargo fmt`；合并前尽量 `cargo clippy --all-targets --all-features -- -D warnings` 无新增警告

## 工具链

必备：

```bash
cargo fmt
cargo clippy --all-targets --all-features -- -D warnings
```

强烈推荐（新项目或已配置项目）：

```bash
cargo nextest run
cargo deny check
cargo machete
taplo fmt
taplo check
```

- `cargo nextest` 优先于默认 `cargo test`；没有安装或项目未配置时用 `cargo test`
- `cargo deny` 用于 license、advisory、重复依赖和供应链检查
- `cargo machete` 用于发现未使用依赖
- `taplo` 用于格式化/检查 `Cargo.toml` 与其他 TOML
- Edition：跟随项目；新 crate 默认 2021+，能选新版本时优先 2024
- 不为小改动强行迁移工具链；已有 CI/Makefile/justfile 时优先跟项目命令

## 命名

| 项 | 风格 |
|----|------|
| crate / 模块 / 函数 / 变量 | `snake_case` |
| 类型 / trait / enum 变体 | `PascalCase` |
| 常量 / 静态 | `SCREAMING_SNAKE_CASE` |
| 生命周期 | 短小：`'a`、`'de` |

## 所有权与 API

1. 能借用就不 `clone`；需要所有权再 `clone` / `to_owned`
2. 优先 `&str` / `&[T]` / `impl AsRef<Path>` 作输入，而不是 `String` / `Vec` / `PathBuf`
3. 返回错误用 `Result<T, E>`；分层见上方硬规则
4. 避免裸 `unwrap` / `expect`（测试与「逻辑上不可能」处除外）；`expect` 须写清原因
5. 需要内部可变或共享状态时，明确选 `Cell`/`RefCell`/`Mutex`/`RwLock`/`Arc`，并说明线程假设
6. `async` 任务要传播 `CancellationToken`/等效取消；`spawn` 的任务要有人接合或明确 detach 理由
7. 跨 `await` 持有 `MutexGuard` 需格外谨慎；优先缩短临界区或改用通道

## 类型与抽象

1. 用 `enum` 表达互斥状态，少用「布尔旗标组合」（详见 `clean-code` 反例）
2. 新类型（tuple struct / thin wrapper）区分不同语义的同型数据
3. trait 边界写在 impl / 函数上够用即可，避免过早抽象
4. 迭代器适配器优先于手写 `for` + 可变累加（可读性更差时除外）
5. `match` 穷尽；通配 `_` 仅在有意忽略时使用

## 模块与可见性

1. 默认私有；只 `pub` 稳定 API
2. `pub(crate)` 用于 crate 内共享
3. 模块按领域拆分，避免巨型 `lib.rs` / `main.rs`
4. 重导出（`pub use`）只暴露有意公开的表面

## 错误与日志

1. 传播用 `?`；在边界转换为调用方需要的错误类型
2. 日志用 `tracing` / `log`，不滥用 `println!` 做诊断
3. 禁止吞掉错误：`let _ = fallible()` 必须注释理由

## 不安全与性能

1. `unsafe` 块尽量小，上方注释不变量与安全条件
2. 先正确再优化；热路径才考虑 `unsafe`、手工 SIMD 等
3. 避免过早 `Box` / 堆分配；大数据结构再评估

## 测试

1. 单元测试靠模块；集成测试放 `tests/`
2. 公共 API 与边界条件要有测试
3. 可用 `#[should_panic]` / `Result` 测试，保持断言具体

## 禁止

- `#[allow(clippy::all)]` 或大范围压制警告
- 无必要的 `mut`
- 在库 API 中泄漏实现细节类型（除非有意）
- 忽略 `Drop` / 资源释放语义
- 库公开 API 使用 `anyhow::Error` 作为稳定错误类型
