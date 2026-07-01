# Dictionaries (Deep Dive)

A dictionary in Python is an unordered (ordered by insertion starting in Python 3.7), changeable collection of key-value pairs. Dictionaries are written with curly braces `{}`.

---

## 1. Accessing Keys safely

Usually, you can access values using square brackets `[]` with the key. However, if the key is missing, Python throws a `KeyError`. Using the `.get()` method prevents this.

```python
person = {"name": "Alice", "age": 30}

# Direct access (raises KeyError if key is missing)
print(person["name"])  # Output: Alice

# Safe access with .get() (returns None if key is missing)
print(person.get("email"))  # Output: None

# Safe access with a default value fallback
print(person.get("email", "N/A"))  # Output: N/A
```

---

## 2. Iterating Over Dictionaries

You can iterate through keys, values, or both (as tuples) in a dictionary.

```python
person = {"name": "Alice", "age": 30, "city": "London"}

# 1. Iterating over keys (default behavior)
for key in person:
    print(key)

# 2. Iterating over values using .values()
for value in person.values():
    print(value)

# 3. Iterating over keys and values using .items() (most common)
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 3. Dictionary Methods Reference

| Method | Description | Example (starting with `d = {"a": 1}`) |
|---|---|---|
| `get(key, default)` | Returns the value of the key (or default if not found). | `d.get("b", 0)` $\rightarrow$ `0` |
| `keys()` | Returns a view object of all keys. | `d.keys()` $\rightarrow$ `dict_keys(['a'])` |
| `values()` | Returns a view object of all values. | `d.values()` $\rightarrow$ `dict_values([1])` |
| `items()` | Returns a view object containing tuples of key-value pairs. | `d.items()` $\rightarrow$ `dict_items([('a', 1)])` |
| `update(other)` | Updates the dictionary with the specified key-value pairs. | `d.update({"b": 2})` $\rightarrow$ `{"a": 1, "b": 2}` |
| `pop(key)` | Removes and returns the value of the specified key. | `d.pop("a")` $\rightarrow$ returns `1`, dict becomes `{}` |
| `setdefault(key, default)` | Returns value of key; if missing, inserts key with default. | `d.setdefault("b", 2)` $\rightarrow$ `d` becomes `{"a": 1, "b": 2}` |
| `clear()` | Removes all elements from the dictionary. | `d.clear()` $\rightarrow$ `{}` |

---

## 4. Merging Dictionaries (Python 3.9+)

In Python 3.9 and above, you can use the union operator `|` to merge two dictionaries. You can also use `|=` to update a dictionary in-place.

```python
defaults = {"theme": "dark", "lang": "en"}
overrides = {"lang": "fr"}

# Merge into a new dictionary
merged = defaults | overrides
print(merged)  # Output: {'theme': 'dark', 'lang': 'fr'} (overrides took precedence)
```

---

## 5. Nested Dictionaries

A dictionary can contain other dictionaries as values.

```python
users = {
    "alice": {"age": 30, "role": "admin"},
    "bob":   {"age": 25, "role": "editor"},
}

print(users["alice"]["role"])  # Output: admin
```

---

## 6. Dictionary Comprehensions

Similar to list comprehensions, you can write concise one-liners to construct dictionaries.

```python
# Creating key-value pairs from a range
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Further Reading

- [Official Python Docs — Mapping Types dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Official Python Docs — Data Structures (Dictionaries)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
