# Rust Style Examples

## Library Error Type

Bad:

```rust
pub fn parse(input: &str) -> Result<Config, anyhow::Error> { /* ... */ }
```

Better:

```rust
#[derive(Debug, thiserror::Error)]
pub enum ParseError { /* ... */ }

pub fn parse(input: &str) -> Result<Config, ParseError> { /* ... */ }
```

## Avoid Unwrap In Production Paths

Bad:

```rust
let port: u16 = env::var("PORT").unwrap().parse().unwrap();
```

Better:

```rust
let port: u16 = env::var("PORT")
    .map_err(...)?
    .parse()
    .map_err(...)?;
```

## Enum State Instead Of Flags

Bad:

```rust
struct Job { started: bool, done: bool, failed: bool }
```

Better:

```rust
enum JobState { Ready, Running, Done, Failed }
```
