# Type Hints

Python is a dynamically typed language, meaning variable types are resolved automatically at runtime. However, starting in Python 3.5, you can add **Type Hints** to document what type a variable, function parameter, or return value is expected to be.

---

## 1. Why Type Hints?

1. **Better Documentation**: Makes your code easier to read and understand.
2. **IDE Support**: Helps IDEs like VS Code and PyCharm provide better autocompletion and highlight potential type errors as you write code.
3. **Static Checking**: You can use external tools like `mypy` to scan your code and find bugs before running it.
4. **Not Enforced**: Python does not enforce type hints at runtime. If you pass a string to a function expecting an integer, the code will still run unless an internal operation fails.

---

## 2. Variable Annotations

You can annotate variables using a colon `:` followed by the type name.

```python
name: str = "Alice"
age: int = 30
is_registered: bool = True

# Standard collections (Python 3.9+)
scores: list[int] = [95, 87, 92]
coordinates: tuple[int, int] = (10, 20)
user_roles: dict[str, str] = {"alice": "admin", "bob": "editor"}
```

---

## 3. Function Annotations

Annotate parameters with `:` and the return type with `->` before the colon.

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

message = greet("Bob", 2)
print(message)  # Output: Hello, Bob! Hello, Bob!
```

---

## 4. Advanced Types: Union and Optional

To write more complex type hints, you can use the standard `typing` module or modern syntax (Python 3.10+).

### Union Types (Multiple possible types)
If a value can be one of several types, use the pipe `|` operator (Python 3.10+) or `Union` (older Python versions).

```python
# Python 3.10+ (Preferred)
def process_value(value: int | float | str) -> str:
    return str(value)

# Older Python versions:
# from typing import Union
# def process_value(value: Union[int, float, str]) -> str:
```

### Optional Types (Type or None)
If a value can be of a specific type or `None`, use `Optional` (from `typing`) or `type | None` (Python 3.10+).

```python
# Python 3.10+ (Preferred)
def find_user(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns string or None

# Older Python versions:
# from typing import Optional
# def find_user(user_id: int) -> Optional[str]:
```

---

## Further Reading

- [Official Python Docs — typing Support for Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 484 — Type Hints Description](https://peps.python.org/pep-0484/)
