# Tuples

A tuple is an **ordered**, **immutable** (unchangeable) sequence of elements. Tuples are written with round brackets `()`.

---

## 1. Why Tuples?

1. **Safety**: Since tuples are immutable, they act as write-protected lists. This ensures data cannot be modified by accident.
2. **Performance**: Tuples are faster than lists and use less memory.
3. **Dictionary Keys**: Since tuples are immutable, they can be used as keys in dictionaries, whereas lists cannot.

---

## 2. Tuple Packing and Unpacking

```python
# Tuple packing
point = (10, 20)

# Tuple unpacking
x, y = point
print(x, y)  # Output: 10 20

# Swapping variables with tuple unpacking
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5
```

---

## 3. Single-Element Tuple Syntax

To create a tuple with only one element, you **must** include a trailing comma. Without it, Python will treat it as a regular string/number wrapped in parentheses.

```python
not_a_tuple = (42)   # Evaluates as type int
is_a_tuple = (42,)   # Evaluates as type tuple
print(type(is_a_tuple))  # Output: <class 'tuple'>
```

---

## 4. Named Tuples

From the standard `collections` module, `namedtuple` allows you to assign names to each position in a tuple, making your code more readable.

```python
from collections import namedtuple

# Defining a named tuple Point
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x, p.y)  # Output: 10 20 (accessed by name instead of index)
```

---

## Further Reading

- [Official Python Docs — Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [python_basics README](../README.md)
