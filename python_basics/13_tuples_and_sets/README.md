# Tuples and Sets

Tuples and Sets are two other core collection data types in Python. While lists are designed to be mutable sequences, tuples and sets serve different, specific purposes.

---

## 1. Tuples

A tuple is an **ordered**, **immutable** (unchangeable) sequence of elements. Tuples are written with round brackets `()`.

### Why Tuples?
1. **Safety**: Since tuples are immutable, they act as write-protected lists. This ensures data cannot be modified by accident.
2. **Performance**: Tuples are faster than lists and use less memory.
3. **Dictionary Keys**: Since tuples are immutable, they can be used as keys in dictionaries, whereas lists cannot.

### Tuple Packing and Unpacking

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

### Single-Element Tuple Syntax
To create a tuple with only one element, you **must** include a trailing comma. Without it, Python will treat it as a regular string/number wrapped in parentheses.

```python
not_a_tuple = (42)   # Evaluates as type int
is_a_tuple = (42,)   # Evaluates as type tuple
print(type(is_a_tuple))  # Output: <class 'tuple'>
```

### Named Tuples
From the standard `collections` module, `namedtuple` allows you to assign names to each position in a tuple, making your code more readable.

```python
from collections import namedtuple

# Defining a named tuple Point
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x, p.y)  # Output: 10 20 (accessed by name instead of index)
```

---

## 2. Sets

A set is an **unordered**, **unindexed** collection of items with **no duplicate elements**. Sets are written with curly braces `{}`.

### Set Basics and Deduplication

```python
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

# Removing duplicates by casting to a set
unique_names = set(names)
print(unique_names)  # Output: {'Alice', 'Bob', 'Charlie'} (unordered)

# Converting back to a list
unique_names_list = list(unique_names)
```

### Adding and Removing Elements
* `add()`: Adds an item.
* `remove()`: Removes an item (raises a `KeyError` if item doesn't exist).
* `discard()`: Removes an item safely (does NOT raise an error if item is missing).

```python
s = {1, 2, 3}
s.add(4)
s.discard(99)  # Does nothing safely
```

### Fast Membership Testing
Checking if an item exists using `in` is extremely fast for sets compared to lists, especially for large datasets.

```python
allowed_users = {"admin", "staff", "editor"}
print("admin" in allowed_users)  # Output: True (runs in O(1) constant time)
```

---

## 3. Mathematical Set Operations

Sets support standard mathematical operations like Union, Intersection, Difference, and Symmetric Difference:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all items from both sets)
print(a | b)  # Output: {1, 2, 3, 4, 5, 6}
# Or: a.union(b)

# Intersection (common items)
print(a & b)  # Output: {3, 4}
# Or: a.intersection(b)

# Difference (in a but not in b)
print(a - b)  # Output: {1, 2}
# Or: a.difference(b)

# Symmetric Difference (items in either a or b, but NOT both)
print(a ^ b)  # Output: {1, 2, 5, 6}
# Or: a.symmetric_difference(b)
```

---

## Further Reading

- [Official Python Docs — Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Official Python Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Official Python Docs — Set Types set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
