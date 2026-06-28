# Variables and Data Types

In Python, variables are containers used to store data, and data types specify the kind of value a variable holds.

## Variables

Unlike languages like C++ or Java, Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

* **Dynamic Typing**: You do not need to specify a variable's data type. The type is determined automatically at runtime, and can even change.

### Example

```python
x = 5       # x is of type int
x = "Sally" # x is now of type str
print(x)
```

## Naming Rules for Variables

* A variable name must start with a letter or the underscore character.
* A variable name cannot start with a number.
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
* Variable names are case-sensitive (`age`, `Age` and `AGE` are three different variables).

---

## Built-in Data Types

Python has several built-in data types grouped into categories. The most common ones are:

### 1. Numeric Types

* **`int`**: Whole numbers, positive or negative, without decimals (e.g., `10`, `-5`).
* **`float`**: Numbers with one or more decimals (e.g., `20.5`, `-0.1`).

### 2. Text Type

* **`str`**: Strings are sequences of characters wrapped in single (`'`) or double (`"`) quotes (e.g., `"Hello World"`, `'Python'`).

### 3. Boolean Type

* **`bool`**: Represents one of two values: `True` or `False`.

### 4. Sequence Types

* **`list`**: An ordered, changeable collection of items. Written with square brackets (e.g., `[1, 2, 3]`).
* **`tuple`**: An ordered, unchangeable collection of items. Written with round brackets (e.g., `(1, 2, 3)`).

### 5. Mapping Type

* **`dict`**: Dictionaries store data in key-value pairs. Written with curly braces (e.g., `{"name": "John", "age": 36}`).

### 6. None Type

* **`NoneType`**: Represents a null value or the absence of a value, written as `None`.

---

## Getting the Data Type

You can get the data type of any object by using the `type()` function:

```python
x = 5
y = "John"
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
```
