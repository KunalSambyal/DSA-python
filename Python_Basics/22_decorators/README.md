# Decorators (Stretch Goal)

Decorators are a powerful feature in Python that allow you to modify or extend the behavior of a function or class without permanently changing its source code.

---

## 1. Functions as First-Class Citizens

To understand decorators, you must first know that in Python, functions are **first-class objects**. This means:

- Functions can be assigned to variables.
- Functions can be passed as arguments to other functions.
- Functions can be returned from other functions.

```python
def greet(name):
    return f"Hello, {name}"

# Assign to variable
say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice
```

---

## 2. What is a Decorator?

A decorator is a function that takes another function as an argument, extends its behavior, and returns a new modified function.

### Example: A simple decorator

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()
# Output:
# Something before the function runs.
# Hi!
# Something after the function runs.
```

---

## 3. Preserving Metadata: `functools.wraps`

When you wrap a function, the original function's name and docstring are replaced by the wrapper's name and docstring. To prevent this, use `functools.wraps` on the wrapper function.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves name and docstring of func
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## 4. Practical Examples

### Example A: Execution Timer Decorator

Times how long a function takes to execute.

```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def compute_squares():
    time.sleep(0.5)
    return [x ** 2 for x in range(1000)]

compute_squares()
```

### Example B: Argument Logging Decorator

Logs function inputs and outputs.

```python
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)
```

---

## 5. Built-in Decorators

Python uses built-in decorators to manage class behaviors:

- **`@classmethod`**: Binds a method to the class rather than the instance.
- **`@staticmethod`**: Defines a utility method that does not access class or instance variables.
- **`@property`**: Defines a getter method (accessed like an attribute) and pairs with a `@name.setter` method for data validation.

---

## Further Reading

- [Official Python Docs — functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)
- [Official Python Docs — Decorators Glossary](https://docs.python.org/3/glossary.html#term-decorator)
