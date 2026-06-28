# Comments and Docstrings

Comments and Docstrings are lines of text in a computer program that explain code behavior to humans. They are ignored by the Python interpreter during execution.

---

## 1. Single-Line Comments

Any text starting with the hash mark (`#`) on a line is treated as a comment. It can stand on its own line or at the end of a line of code.

```python
# This is a comment on its own line
print("Hello, World!")

print("Welcome to Python!")  # This is an inline comment
```

---

## 2. Multi-Line Comments

Python does not have a specific syntax for multi-line comments. To write comments spanning multiple lines, you can use:

### Multiple Hash Marks

```python
# This is a comment
# that spans across
# multiple lines.
```

### Multi-line String Literals (With Caution)

Since Python ignores string literals that are not assigned to a variable, you can use triple quotes (`"""` or `'''`) to write comments:

```python
"""
This is a multi-line string
that acts as a comment because it
is not assigned to any variable.
"""
print("Hello, World!")
```

- **Important Note**: Triple-quoted strings are technically **string literals**, not actual comments. Python compiles them into bytecode, which can introduce minor performance and memory overhead if placed inside functions.

---

## 3. Proper Docstring Usage

Docstrings (Documentation Strings) are triple-quoted string literals placed immediately as the first statement inside a function, class, or module. Unlike comments, docstrings are preserved by Python and can be accessed dynamically at runtime using the `__doc__` attribute or the built-in `help()` function.

### Example: Proper Docstring Structure

```python
def add(a, b):
    """
    Returns the sum of a and b.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b

# Accessing the docstring
print(add.__doc__)
```

---

## Further Reading

- [Official Python Docs — Documentation Strings](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
