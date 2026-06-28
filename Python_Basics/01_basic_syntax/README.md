# Basic Syntax

Python syntax is designed to be readable and clean, looking very similar to the English language. 

## Python Indentation

In most programming languages, curly braces `{}` or keywords are used to define a block of code (like a loop or function body). In Python, block definition is done using **indentation** (whitespace at the beginning of a line).

* You must use the same number of spaces in the same block of code, otherwise Python will throw an `IndentationError`.
* The standard practice is to use **4 spaces** for indentation.

### Example

```python
if 5 > 2:
    print("Five is greater than two!")
```

If you do not indent, Python will output an error:

```python
# This will cause an IndentationError:
if 5 > 2:
print("Five is greater than two!")
```

## Statement Multi-line Continuation

In Python, a new line signifies the end of a statement. However, you can write a single statement across multiple lines using the backslash (`\`) continuation character.

### Example

```python
total = 1 + \
        2 + \
        3
print(total)  # Output: 6
```

## Semicolons

Unlike languages such as C++ or Java, Python does not require a semicolon (`;`) at the end of statements. Semicolons are optional and can be used to write multiple statements on a single line, though this is generally discouraged for readability.

### Example

```python
print("Hello"); print("World")
```
