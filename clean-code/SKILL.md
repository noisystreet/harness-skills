---
name: clean-code
description: >-
  Apply language-agnostic clean code rules for readable, maintainable software.
  Use when writing, refactoring, or reviewing code of any language; when the user
  mentions clean code, readability, code quality, naming, or structure.
  Language-specific idioms defer to rust-style, cpp-style, python-style, or other *-style skills.
---

# Clean Code

跨语言的可读性与可维护性约束。  
**语言惯用法、工具链、所有权等** → 见 `rust-style` / `cpp-style` / `python-style`（及其他 `*-style`）。本 skill 不覆盖语言特例。

## 命名

1. 名字表达意图与用途，不缩写除非领域通行（如 `id`、`ctx`、`http`）
2. 禁止无意义名：`tmp`、`data2`、`foo`、`obj`（极短生命周期的循环变量除外）
3. 布尔用 `is_` / `has_` / `can_` / `should_` 等可读前缀（跟语言惯例）
4. 类型/函数名与行为一致；避免「ProcessData」这类空泛动词堆砌

## 函数与模块

1. 一个函数一件事；难用一句话说清职责就拆
2. 参数宜少；多个布尔旗标改为枚举、选项对象或拆成多个函数
3. 层次一致：同一函数内不要混「业务编排」与「底层细节」太深
4. 模块按领域/职责边界划分，不按「Utils 大杂烩」无限膨胀
5. 重复逻辑在第三次出现前考虑抽取；过早抽象也不要

## 控制流与结构

1. 早返回减少嵌套；避免深层 `if/else` 金字塔
2. 错误与成功路径分离；不要把异常/错误埋在正常逻辑中间
3. 用合适的数据结构消除复杂分支（查表、策略、状态机），而不是堆条件
4. 魔法数/魔法字符串抽成命名常量（除非字面量本身即领域含义且仅一处）

## 副作用与状态

1. **减少隐式状态**：避免用散落的可变旗标/缓存/「上次结果」成员在远处影响行为；状态应局部、显式、可命名
2. 能当参数或返回值传递的，不要藏进对象字段或全局/线程局部里「顺便带过去」
3. 纯计算与 IO/可变状态分开，便于测、便于读
4. 可变状态范围尽量小；谁拥有、谁修改写清楚
5. 需要状态机时用显式状态类型（枚举/代数类型），禁止一堆布尔组合伪装状态
6. 函数要么查询要么命令，避免「改状态又返回复杂结果」的隐式耦合（合理的 fluent API 除外）

## 注释与文档

1. 注释写「为什么」和非常规约束，不写「代码在干什么」
2. 过时注释比没有更糟；改代码时同步改注释
3. 公开 API 用语言惯用文档（doc comment）；内部实现少而精

## 错误处理

1. 失败必须显式：返回错误、抛异常或传播——禁止静默吞掉
2. 在合适边界转化错误（用户可读 vs 内部诊断），不要层层丢上下文
3. 断言/panic 仅用于「不可能发生」的不变量，不用于可预期的用户/输入错误

## 测试与可验证性

1. 改行为时同步考虑测试；公共行为与边界条件优先
2. 可测性差（强单例、全局可变、时间/随机写死）先隔离依赖再堆逻辑
3. 测试名说明场景与期望，避免 `test1`

## 反例 → 改法

### 1. 布尔组合伪装状态

```text
# 反例
started=false, done=false, failed=false  # 非法组合多，分支爆炸

# 改法：显式状态
enum Phase { Ready, Running, Done, Failed }
```

### 2. 隐式成员状态「远处生效」

```text
# 反例
obj.cache = load()          # 别处读 cache，调用方看不见依赖
obj.process()               # 行为取决于谁先设了 cache

# 改法：参数 / 返回值显式传递
data = load()
obj.process(data)           # 或 process() -> Result 自带所需数据
```

### 3. 查询却偷改状态

```text
# 反例
count = registry.get_count()   # 内部顺便 flush / 清标志 / 写日志副作用

# 改法：分开
registry.flush()
count = registry.count()       # 纯查询无副作用
```

## 审查时优先报

按严重度提，不空谈风格：

1. 错误被吞、资源/生命周期不清、行为与命名不符
2. 隐式/散落可变状态、布尔旗标丛生伪装状态机
3. 过长函数、过深嵌套、无意义命名、无故重复、误导性注释

## 禁止

- 为「看起来干净」做无行为变化的大规模重命名/搬文件（除非用户要求重构）
- 引入与项目既有风格冲突的新风格（同一 PR 内保持一致）
- 用空泛原则替代具体修改建议
