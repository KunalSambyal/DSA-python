# Basic Syntax

Python syntax is designed to be readable and clean, looking very similar to the English language.

## Python Indentation

In most programming languages, curly braces `{}` or keywords are used to define a block of code. In Python, block definition is done using **indentation** (whitespace at the beginning of a line).

- You must use the same number of spaces in the same block of code, otherwise Python will throw an `IndentationError`.
- The standard practice is to use **4 spaces** for indentation.

### Example

```python
if 5 > 2:
    print("Five is greater than two!")
```

---

## Line Continuation

In Python, a new line signifies the end of a statement. However, if a statement is long, it can be split across multiple lines.

### 1. Implicit Line Continuation (Preferred)

You can split statements inside parentheses `()`, brackets `[]`, or braces `{}` without using any continuation characters. This is the preferred style in Python.

```python
# Preferred: implicit continuation inside parentheses
total = (1 +
         2 +
         3)
print(total)  # Output: 6
```

### 2. Explicit Line Continuation

You can write a single statement across multiple lines using the backslash (`\`) continuation character.

```python
total = 1 + \
        2 + \
        3
print(total)  # Output: 6
```

---

## The `pass` Statement

The `pass` statement is a null operation. It does nothing when executed. It is used as a placeholder when a statement is syntactically required but you do not want to run any code yet.

```python
# Placeholder for a function to be implemented later
def future_function():
    pass
```

---

## Semicolons

Unlike languages such as C++ or Java, Python does not require a semicolon (`;`) at the end of statements. Semicolons are optional and can be used to write multiple statements on a single line, though this is generally discouraged for readability.

```python
print("Hello"); print("World")
```

---

## PEP 8 Style Guide

PEP 8 is the official style guide for writing Python code. It provides guidelines on formatting code to make it as readable and consistent as possible. Following PEP 8 is highly recommended for all Python developers.

---

## Further Reading

- [Official Python Docs — Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
