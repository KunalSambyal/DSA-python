# Comprehensions

Comprehensions in Python provide a concise way to create new collections (lists, sets, dictionaries) from existing iterables. They are often more readable and faster than writing traditional loops.

---

## 1. List Comprehensions

List comprehensions allow you to construct lists in a single line.

### Basic Syntax
```python
# Syntax: [expression for item in iterable]
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

### With a Condition (Filtering)
You can add an `if` clause at the end to filter elements.
```python
# Syntax: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

### Nested List Comprehensions
You can nest comprehensions to perform operations on multi-dimensional lists (like flattening a matrix).

```python
matrix = [[1, 2], [3, 4], [5, 6]]

# Flattening the matrix
flat = [num for row in matrix for num in row]
print(flat)  # Output: [1, 2, 3, 4, 5, 6]
```

---

## 2. Set and Dictionary Comprehensions

### Set Comprehensions
Constructs a set (removing duplicate results). Syntax is similar to list comprehensions but uses curly braces `{}`.

```python
# Get unique lengths of words
words = ["apple", "banana", "kiwi", "fig"]
lengths = {len(word) for word in words}
print(lengths)  # Output: {3, 4, 5, 6}
```

### Dictionary Comprehensions
Constructs a dictionary using key-value pairs.

```python
# Syntax: {key_expr: value_expr for item in iterable}
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}
```

---

## 3. Generator Expressions (Lazy Evaluation)

A generator expression uses the exact same syntax as a list comprehension, but wraps it in round parentheses `()` instead of square brackets `[]`.

Unlike list comprehensions, **generators do not store the entire collection in memory**. Instead, they yield items one at a time on-demand (lazy evaluation), which is highly memory-efficient for large datasets.

```python
import sys

# List comprehension: builds the entire list in memory
list_result = [x ** 2 for x in range(10000)]

# Generator expression: computes values one-by-one as requested
gen_result = (x ** 2 for x in range(10000))

# Comparing memory consumption (bytes)
print(sys.getsizeof(list_result))  # Output: ~85160 bytes
print(sys.getsizeof(gen_result))   # Output: ~104 bytes (very small!)
```

---

## 4. Best Practices: Comprehension vs. Loop

* **Use a comprehension** when you are doing a simple transformation or filtering operation on a collection. It makes the code clean and readable.
* **Use a regular loop** if your logic is complex, requires multiple lines of code, has multiple nested loops, or performs side effects (like print statements, file writes, or database queries). Writing nested comprehensions beyond two levels is generally discouraged as it ruins readability.

---

## Further Reading

- [Official Python Docs — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Official Python Docs — Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
