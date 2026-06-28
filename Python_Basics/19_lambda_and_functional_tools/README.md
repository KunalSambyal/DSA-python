# Lambda Functions and Functional Tools

Python supports functional programming features. In addition to regular functions, Python allows you to write anonymous functions (`lambda` functions) and use them with built-in tools like `map()`, `filter()`, and `sorted()`.

---

## 1. Lambda Functions Syntax

A lambda function is a small, anonymous function (a function without a name). It can take any number of arguments, but can only have a single expression.

```python
# Syntax: lambda arguments: expression
double = lambda x: x * 2
print(double(5))  # Output: 10

multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12
```

### When to Use?
Use lambda functions as short, "throwaway" functions that are passed directly as arguments to other functions.

---

## 2. Functional Tools

### The `map()` Function
`map()` applies a specified function to every item in an iterable (like a list) and returns a map object (which can be cast back into a list).

```python
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

### The `filter()` Function
`filter()` creates an iterator from elements of an iterable for which a function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
```

### `sorted()` with a `key`
You can sort complex structures by passing a lambda function as the `key` argument to `sorted()`.

```python
students = [
    {"name": "Charlie", "grade": 85},
    {"name": "Alice",   "grade": 92},
    {"name": "Bob",     "grade": 78},
]

# Sort students by grade (descending)
ranked = sorted(students, key=lambda s: s["grade"], reverse=True)
for student in ranked:
    print(student["name"], student["grade"])
```

---

## 3. Best Practice: Comprehensions vs. `map()`/`filter()`

While `map()` and `filter()` are standard in many functional programming languages, in Python, **list comprehensions are generally preferred** because they are considered more readable and idiomatic.

```python
numbers = [1, 2, 3, 4, 5]

# Using map/filter (requires casting back to list)
doubled = list(map(lambda x: x * 2, numbers))

# Using List Comprehension (simpler and more readable)
doubled_comp = [x * 2 for x in numbers]
```

---

## Further Reading

- [Official Python Docs — Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Official Python Docs — Built-in Functions: map](https://docs.python.org/3/library/functions.html#map)
- [Official Python Docs — Built-in Functions: filter](https://docs.python.org/3/library/functions.html#filter)
