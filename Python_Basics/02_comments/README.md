# Comments

Comments are lines of text in a computer program that are ignored by the compiler or interpreter. They are used to explain the purpose of the code, making it easier for humans to read and maintain.

## Single-Line Comments

In Python, any text starting with the hash mark (`#`) on a line is treated as a comment. The comment can be on its own line or at the end of a line of code.

### Examples

```python
# This is a single-line comment on its own line
print("Hello, World!")

print("Welcome to Python!")  # This is an inline comment
```

## Multi-Line Comments

Python does not have a specific syntax for multi-line comments. To write a comment that spans multiple lines, you can use either of the following approaches:

### 1. Multiple Hash Marks

You can insert a `#` on each line:

```python
# This is a comment
# that spans across
# multiple lines.
print("Hello, World!")
```

### 2. Multi-line String Literals (Docstrings)

Since Python ignores string literals that are not assigned to a variable, you can use a multi-line string (triple quotes `"""` or `'''`) to write comments:

```python
"""
This is a multi-line string
that is not assigned to any variable.
Python will ignore it, so it acts
as a comment.
"""
print("Hello, World!")
```
