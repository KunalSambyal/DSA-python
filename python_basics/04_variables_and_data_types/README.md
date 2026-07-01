# Variables and Data Types

In Python, variables are containers used to store data, and data types specify the kind of value a variable holds.

---

## 1. Variables

A variable is created the moment you first assign a value to it.

- **Dynamic Typing**: Python has no command for declaring a variable. The type is determined automatically at runtime, and can change.

```python
x = 5       # x is of type int
x = "Sally" # x is now of type str
```

### Variable Naming Rules

- Must start with a letter or the underscore character (`_`).
- Cannot start with a number.
- Can only contain alphanumeric characters and underscores (`A-z`, `0-9`, and `_`).
- Are case-sensitive (`age`, `Age`, and `AGE` are different variables).

---

## 2. Multiple Assignment and Unpacking

Python allows you to assign values to multiple variables in a single line.

```python
# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3

# Swap variables without a temporary variable
a, b = b, a
print(a, b)  # Output: 2 1
```

---

## 3. Core Data Types

### Numeric Types

- **`int`**: Whole numbers (e.g., `10`, `-5`).
- **`float`**: Decimals (e.g., `20.5`, `-0.1`).
- **`complex`**: Complex numbers written with a `j` for the imaginary part (e.g., `z = 1 + 2j`).

### Sequence Types

- **`str`**: Strings are sequences of characters wrapped in quotes.
- **`list`**: Ordered, changeable collection (e.g., `[1, 2, 3]`).
- **`tuple`**: Ordered, unchangeable collection (e.g., `(1, 2, 3)`).

### Mapping Type

- **`dict`**: Key-value pairs (e.g., `{"name": "John", "age": 36}`).

### Set Type

- **`set`**: An unordered, unindexed collection with no duplicate elements.

```python
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # Output: {1, 2, 3} (duplicates automatically removed)
```

### Other Types

- **`bool`**: Logical values (`True` or `False`).
- **`NoneType`**: Represents a null value (`None`).

---

## 4. Basic String Operations

Strings are sequences of characters. You can inspect, slice, and modify them.

### Slicing

Get a range of characters using the syntax `[start:end]` (excluding the end index).

```python
text = "Python"
print(text[0:2])  # Output: Py
print(text[2:5])  # Output: tho
```

### Common String Methods

String methods return new values without changing the original string (strings are immutable).

```python
text = "  Hello, World!  "
print(text.strip())          # Output: "Hello, World!" (removes outer spacing)
print(text.lower())          # Output: "  hello, world!  "
print(text.upper())          # Output: "  HELLO, WORLD!  "
print("a,b,c".split(","))   # Output: ['a', 'b', 'c']
print("-".join(["a", "b", "c"])) # Output: a-b-c
```

---

## Common Mistakes

### Confusing `=` with `==`

- The single equals sign `=` is the **assignment operator**, used to set a variable.
- The double equals sign `==` is a **comparison operator**, used to check equality.

```python
x = 5  # Assigns the value 5 to x

# Incorrect (will raise a SyntaxError in an if statement):
# if x = 5:

# Correct:
if x == 5:
    print("x is 5")
```

---

## Further Reading

- [Official Python Docs — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Official Python Docs — Variables and Types](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
