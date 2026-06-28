# Modules and Packages

As your codebase grows, you should organize your code into multiple files (Modules) and directories (Packages) to keep it clean and maintainable.

---

## 1. What is a Module?

A **Module** is simply a Python file (ending in `.py`) that contains executable statements, function definitions, or class definitions.

### Example: Creating and Importing a Module
Suppose you create a file named `mymath.py` with the following content:

```python
# mymath.py
def add(a, b):
    return a + b

def square(x):
    return x ** 2
```

You can now use this module in another Python file (`main.py`) in the same directory:

```python
# main.py

# Method 1: Import the whole module
import mymath
print(mymath.add(5, 10))  # Output: 15

# Method 2: Import specific functions
from mymath import square
print(square(4))  # Output: 16

# Method 3: Import and rename (alias)
import mymath as mm
print(mm.add(1, 2))  # Output: 3
```

*Note: Avoid using `from module import *` as it imports all names into the current namespace, which can lead to name clashes and makes code hard to read.*

---

## 2. The `__name__ == "__main__"` Guard

When a Python file is run directly, its special global variable `__name__` is set to `"__main__"`. If the file is imported by another script, `__name__` is set to the file's name.

Using this guard allows you to write testing code that *only* runs when you execute the file directly, and does not run when someone imports your module.

```python
# mymath.py
def add(a, b):
    return a + b

# This code block will NOT run when main.py imports mymath
if __name__ == "__main__":
    print("Testing mymath module directly:")
    print(add(10, 20))
```

---

## 3. What is a Package?

A **Package** is a folder containing multiple Python modules. Packages allow you to group related modules together in a directory structure.

### Package Directory Structure
To make Python treat a directory as a package, it must contain a file named `__init__.py` (this file can be completely empty, but it is required).

```text
myproject/
│
├── main.py
└── mypackage/
    ├── __init__.py
    ├── geometry.py
    └── algebra.py
```

### Importing from a Package
You can import modules from packages using dot notation:

```python
# In main.py
from mypackage import geometry
from mypackage.algebra import add
```

---

## 4. Absolute vs. Relative Imports

* **Absolute Imports**: Specify the full path to the module from the project's root folder. Highly readable and preferred.
  ```python
  from mypackage.algebra import add
  ```
* **Relative Imports**: Use dot `.` notation to import relative to the current module's location.
  * `.` means the current directory.
  * `..` means the parent directory.
  ```python
  from .algebra import add  # Import from algebra module in same directory
  ```

---

## Further Reading

- [Official Python Docs — Modules](https://docs.python.org/3/tutorial/modules.html)
- [Official Python Docs — Packages](https://docs.python.org/3/tutorial/modules.html#packages)
