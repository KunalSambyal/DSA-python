# Standard Library Modules

Python includes a rich set of built-in modules (the Standard Library) that solve common programming problems out-of-the-box. 

---

## 1. The `os` Module (Operating System)
Used for interacting with the operating system, navigating directories, and reading environment variables.

```python
import os

print(os.getcwd())             # Get current working directory
print(os.listdir("."))         # List all files/folders in the current directory
os.makedirs("new_dir", exist_ok=True)  # Create a directory safely (no error if it exists)
```

---

## 2. The `sys` Module (System)
Used to access system-specific parameters and functions (like command-line arguments and Python interpreter versions).

```python
import sys

print(sys.version)  # Prints current Python version details
print(sys.argv)     # List of command line arguments passed to the script
```

---

## 3. The `random` Module
Used to generate pseudo-random numbers, choose random items, or shuffle lists.

```python
import random

print(random.randint(1, 10))  # Random integer between 1 and 10 (inclusive)

items = ["apple", "banana", "cherry"]
print(random.choice(items))   # Picks a random item from the list

random.shuffle(items)         # Shuffles the list in-place
print(items)
```

---

## 4. The `collections` Module
Provides specialized container data types to supplement Python's general-purpose built-ins.

### `Counter`
A dict subclass for counting hashable objects.

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)  # Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(count.most_common(1))  # Output: [('apple', 3)]
```

### `defaultdict`
A dict subclass that calls a factory function to supply missing values, avoiding `KeyError`.

```python
from collections import defaultdict

# Creates a list for any new key automatically
grouped_data = defaultdict(list)
grouped_data["fruits"].append("apple")
print(grouped_data)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple']})
```

---

## 5. Standard Modules Recap (Math, JSON, Datetime, Pathlib)

* **`math`**: Math functions and constants (`math.sqrt()`, `math.ceil()`, `math.floor()`, `math.pi`).
* **`json`**: Serializing and parsing JSON strings and files (`json.loads()`, `json.dumps()`, `json.load()`, `json.dump()`).
* **`datetime`**: Date and time manipulation (`datetime.datetime.now()`, `strftime()`).
* **`pathlib`**: Modern object-oriented path handling (`Path("my_folder") / "file.txt"`).

---

## Further Reading

- [Official Python Docs — The Python Standard Library](https://docs.python.org/3/library/)
- [Official Python Docs — random module](https://docs.python.org/3/library/random.html)
- [Official Python Docs — collections module](https://docs.python.org/3/library/collections.html)
