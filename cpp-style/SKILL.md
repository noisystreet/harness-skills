---
name: cpp-style
description: >-
  Apply modern C++ coding standards (C++17/20 idioms, RAII, safety, clarity).
  Use when writing, refactoring, or reviewing C++ code, CMake/Bazel C++ targets,
  or when the user mentions C++ style / guidelines / Modern C++ / CMake /
  clang-format / clang-tidy.
  General readability rules defer to clean-code; this skill owns C++-specific rules.
---

# C++ 编程规范

以 Modern C++（默认 C++17/20，跟随项目）为准：RAII、类型安全、可读性优先。新项目强烈推荐 CMake + clang-format。
**命名意图、隐式状态、函数拆分等通用规则** → 见 `clean-code`。本文件只定 C++ 特例。
优秀项目、教材和官方资料 → 见 [reference.md](reference.md)。

## 硬规则（默认）

项目另有约定时跟项目；否则按此执行：

1. **RAII 必须**：禁止配对裸 `new`/`delete`；对接 C API 时立刻包进智能指针 / 专有句柄类型
2. **所有权默认 `unique_ptr`**；`shared_ptr` 仅在确实共享生命周期时使用
3. **异常策略二选一且贯彻**：项目启用异常则保证至少基本异常安全；禁用异常则不用 `throw`，错误用返回类型（`optional`/`expected`/错误码）
4. **`enum class`** 表达互斥状态；禁止多布尔成员伪装状态机（见 `clean-code` 反例）
5. 头文件禁止 `using namespace std;`；不抛无边界的所有权裸指针
6. 优先 `override`、`nullptr`、列表初始化 `{ }`；禁止 C 风格强转（`reinterpret_cast` 需书面理由）
7. 新项目强烈推荐 **CMake** 组织构建、**clang-format** 统一格式；已有项目跟随其构建/格式化工具

## 语言与工具

必备/强烈推荐：

```bash
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build
ctest --test-dir build --output-on-failure
clang-format -i <files>
```

推荐静态检查（项目已配置或改动较大时）：

```bash
clang-tidy <files> -p build
```

- 新项目强烈推荐 CMake；既有项目用 Bazel/Make/Meson 等时跟随项目，不为小改动强行迁移
- 新项目必须提供 `.clang-format`；无项目配置时保持邻近代码一致，不大规模重排
- CMake 项目建议开启 `CMAKE_EXPORT_COMPILE_COMMANDS=ON`，便于 clangd/clang-tidy
- 标准：跟随项目；新代码避免无故使用早于项目标准的写法
- 能用标准库就不用自造轮子（`std::vector`、`string_view`、`optional`、`span` 等）

## 命名

| 项 | 风格 |
|----|------|
| 类型 / 模板参数 | `PascalCase` 或项目既有风格 |
| 函数 / 变量 | `snake_case` 或项目既有风格 |
| 常量 | `kConstant` 或 `SCREAMING_SNAKE`（跟项目） |
| 宏 | `SCREAMING_SNAKE`，尽量少用 |
| 成员 | 与项目一致（`m_` / 尾下划线 / 无前缀） |

**同一文件 / 同一 PR 内不要混用新风格与旧风格。**

## 资源与所有权

1. 一切资源用 RAII；禁止裸 `new`/`delete`（除非对接旧 API 并立即包进智能指针）
2. 独占所有权：`std::unique_ptr`；共享：`std::shared_ptr`（默认先考虑 unique）
3. 观察指针 / 引用不拥有对象；文档写清生命周期
4. 容器与字符串优先值语义；大对象再考虑移动 / 指针

## 接口设计

1. 输入：只读用 `const T&` 或 `std::string_view` / `std::span`；要所有权再用值 / 右值引用
2. 输出参数少用；优先返回值（含 `struct` / `optional` / `expected`）
3. 可失败操作用 `std::optional`、`std::expected`（C++23）或项目错误类型；避免「魔法」返回码散落
4. `const` 正确性：不修改的对象 / 成员函数标 `const`
5. `override` 标注虚函数覆写；析构函数在基类中按需 `virtual`

## 现代惯用法

1. `auto` 用于类型冗长或显而易见处；返回类型或 API 边界宜写明类型
2. 范围 `for`、`nullptr`、`enum class`、scoped enum
3. 优先 `= default` / `= delete` 控制特殊成员函数
4. 移动：需要时提供移动构造 / 赋值；遵守规则五 / 规则零
5. 模板：约束用 concepts（C++20）或 `enable_if`；错误信息要可读
6. 避免宏做逻辑；常量用 `constexpr` / `consteval`

## 安全与正确性

1. 禁止无界 C 数组与原始指针算术（除非性能关键路径且有审查）
2. 整数：注意符号 / 窄化；用 `{ }` 列表初始化避免窄化
3. 线程：共享可变状态必须同步；默认假设数据竞争是 bug
4. 头文件：include guard 或 `#pragma once`；只 include 用到的头；前向声明减依赖
5. 不在头文件里用 `using namespace std;`

## 错误处理

1. 构造失败：考虑工厂函数返回 `optional`/`expected`，或文档化异常
2. 异常：要么异常安全（至少基本保证），要么项目明确禁用异常并贯彻到底（见硬规则）
3. 断言：`assert` / 项目 CHECK 用于不变量；不用于可恢复的用户错误

## 禁止

- 手动内存管理绕过 RAII「因为简单」
- C 风格强转；用 `static_cast` / `const_cast` / `reinterpret_cast`（后者需强理由）
- 无所有权约定的裸指针在模块间传来传去
- 复制粘贴重复逻辑而不抽取（合理复杂度内）
- 多布尔成员伪装状态机、头文件 `using namespace std;`
