# Sets

A set is an **unordered**, **unindexed** collection of items with **no duplicate elements**. Sets are written with curly braces `{}`.

---

## 1. Set Basics and Deduplication

```python
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

# Removing duplicates by casting to a set
unique_names = set(names)
print(unique_names)  # Output: {'Alice', 'Bob', 'Charlie'} (unordered)

# Converting back to a list
unique_names_list = list(unique_names)
```

---

## 2. Adding and Removing Elements

* `add()`: Adds an item.
* `remove()`: Removes an item (raises a `KeyError` if item doesn't exist).
* `discard()`: Removes an item safely (does NOT raise an error if item is missing).

```python
s = {1, 2, 3}
s.add(4)
s.discard(99)  # Does nothing safely
```

---

## 3. Fast Membership Testing

Checking if an item exists using `in` is extremely fast for sets compared to lists, especially for large datasets.

```python
allowed_users = {"admin", "staff", "editor"}
print("admin" in allowed_users)  # Output: True (runs in O(1) constant time)
```

---

## 4. Mathematical Set Operations

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

- [Official Python Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Official Python Docs — Set Types set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [python_basics README](../README.md)
