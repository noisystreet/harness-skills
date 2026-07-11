# C++ Style Examples

## RAII Over Manual New/Delete

Bad:

```cpp
auto* buf = new Buffer();
use(buf);
delete buf;
```

Better:

```cpp
auto buf = std::make_unique<Buffer>();
use(*buf);
```

## Enum Class For States

Bad:

```cpp
bool started = false;
bool done = false;
bool failed = false;
```

Better:

```cpp
enum class Phase { Ready, Running, Done, Failed };
```

## Prefer Return Values

Bad:

```cpp
bool load(Config& out);  // unclear failure + output mix
```

Better:

```cpp
std::optional<Config> load();
// or std::expected<Config, Error> on C++23 projects
```
