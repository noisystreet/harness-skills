---
name: python-style
description: >-
  Apply idiomatic modern Python coding standards with strong preference for uv,
  ruff, type hints, and pytest.
  Use when writing, refactoring, or reviewing Python code, or when the user
  mentions Python style / PEP 8 / type hints / pytest / uv / ruff.
  General readability rules defer to clean-code; this skill owns Python-specific rules.
---

# Python 编程规范

以可读、惯用的现代 Python（默认 3.10+，新项目推荐 3.12+）为准。  
**命名意图、隐式状态、函数拆分等通用规则** → 见 `clean-code`。本文件只定 Python 特例。

## 硬规则（默认）

项目另有约定时跟项目；否则按此执行：

1. **新项目强烈推荐 `uv`** 管 Python 版本、虚拟环境、依赖和命令运行；既有项目跟随其包管理器
2. **格式与静态检查强烈推荐 `ruff`**：优先 `ruff check` + `ruff format`，不要新引入 black/isort/flake8 组合，除非项目已使用
3. **公开 API 加类型标注**；内部复杂函数也尽量标；类型检查优先 `pyright`（或跟项目 mypy/pyright）
4. `# type: ignore` / `# noqa` 必须窄范围并写理由，禁止大面积压制
5. **异常**：不裸 `except:` / `except Exception:` 后静默吞掉；捕获要具体，或记录后重新抛出
6. **互斥状态用 `Enum` / 代数式联合**，不用多布尔字段组合（见 `clean-code` 反例）
7. 路径用 `pathlib.Path`；文本默认 UTF-8；避免无必要的字符串拼路径
8. 依赖与环境：优先 `pyproject.toml`；不擅自引入未声明的重量级依赖
9. 测试用 **pytest**（项目另有框架除外）；新行为尽量带测

## 工具链

默认命令（新项目或已使用 uv/ruff 的项目）：

```bash
uv run ruff format .
uv run ruff check .
uv run pytest
```

可选类型检查：

```bash
uv run pyright
```

- 既有项目已有命令时优先跟项目（如 `make test`、`tox`、`nox`）
- 没有 `uv` 时使用项目当前环境运行同等命令，不为小改动强行迁移工具链
- 有类型检查配置时跑通或说明未跑原因

## 命名

| 项 | 风格 |
|----|------|
| 模块 / 函数 / 变量 | `snake_case` |
| 类 / 异常类型 / `Enum` | `PascalCase` |
| 常量 | `SCREAMING_SNAKE_CASE` |
| 伪私有 | 单前导下划线 `_name` |
| 包名 | 短、全小写；避免无必要下划线 |

## 类型与接口

1. 用 `list[T]`、`dict[K, V]`、`X | None`（3.10+）；旧项目可跟其 `Optional`/`List` 写法
2. 结构化数据优先 `dataclass` / `NamedTuple` / pydantic（项目已用时）；少用无文档的裸 `dict` 当核心模型
3. 入参：能接受抽象就别绑死具体（如可读 `Iterable` 而非必须 `list`），但不要过度泛化
4. 返回 `None` 表示「无结果」要在类型与文档中明确；失败用异常或 `Result` 式类型，别用魔法返回值

## 错误与资源

1. 用具体异常类型；自定义异常继承合适基类，带清晰消息
2. 资源用 `with`（文件、锁、连接）；禁止依赖 `__del__` 做清理
3. 禁止 `except: pass`；`contextlib.suppress` 仅用于明确可忽略的窄异常
4. 库代码少在深层 `print`；用 `logging`，由应用配置 handler

## 模块与结构

1. 模块按职责拆分；避免巨型「god module」与无边界的 `utils.py`
2. `import` 放文件顶部（惯例例外：延迟导入破循环 / 可选依赖，并注释原因）
3. 相对导入用于包内；对外入口保持稳定
4. `__all__` 仅在有意控制 `from pkg import *` 或公开表面时使用

## 简洁与惯用

1. 推导式保持短小可读；复杂逻辑用显式循环
2. 用 `dataclass`/`Enum`/模式匹配（3.10+ `match`）表达结构，减少旗标丛生
3. 不要为「看起来函数式」而牺牲可读性（过度 `lambda` / 嵌套推导）
4. 可变默认参数禁止：`def f(x=[])` → 用 `None` + 函数内初始化

## 测试

1. 测试文件/函数：`test_*.py` / `test_*`
2. 断言具体；需要时用 `pytest.raises`、`parametrize`
3. 固定时间、随机、网络：夹具或 mock，不依赖脆弱外部环境

## 禁止

- 裸 `except:` 或吞掉异常不记录
- 可变默认参数
- 无理由的 `# type: ignore`、大面积 `# noqa`
- 在库深层乱 `print` 当日志
- 多布尔伪装状态机、无类型的公开 API（新代码）
