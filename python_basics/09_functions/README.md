# Functions

A function is a reusable block of code that only runs when it is called. You can pass data (parameters) into a function, and a function can return data as a result.

---

## 1. Defining and Calling a Function

In Python, a function is defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. 

```python
# Definition
def greet(name):
    """Prints a friendly greeting."""
    print(f"Hello, {name}!")

# Call
greet("Alice")
```

---

## 2. Arguments and Parameters

* **Parameter**: The variable listed inside the parentheses in the function definition (e.g., `name` in `def greet(name):`).
* **Argument**: The actual value sent to the function when called (e.g., `"Alice"` in `greet("Alice")`).

### Default Parameter Values
You can specify default values for parameters. If the function is called without that argument, it uses the default value.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")            # Output: Hello, Alice!
greet("Bob", "Welcome")  # Output: Welcome, Bob!
```

### Keyword Arguments
You can send arguments using the `key = value` syntax. In this case, the order of the arguments does not matter.

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

# Keyword arguments
describe_pet(name="Buddy", animal="dog")
```

---

## 3. Variable-Length Arguments

If you do not know how many arguments will be passed into your function, use `*args` or `**kwargs`.

### `*args` (Positional Arguments)
Accepts any number of positional arguments as a **tuple**.

```python
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))  # Output: 10
```

### `**kwargs` (Keyword Arguments)
Accepts any number of keyword arguments as a **dictionary**.

```python
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="London")
```

---

## 4. Variable Scope

* **Local Variable**: Defined inside a function; accessible only within that function.
* **Global Variable**: Defined in the main body of the script; accessible everywhere.
* **`global` Keyword**: Used to modify a global variable inside a function.

```python
x = 10  # Global variable

def my_func():
    x = 20  # Local variable (does not affect the global x)
    print(f"Inside: {x}")

my_func()   # Output: Inside: 20
print(f"Outside: {x}")  # Output: Outside: 10

# Modifying global variable
def change_global():
    global x
    x = 30

change_global()
print(f"New Global: {x}")  # Output: New Global: 30
```

---

## 5. Lambda (Anonymous) Functions

A lambda function is a small, anonymous function that can take any number of arguments but can only have one expression.

```python
# Syntax: lambda arguments: expression
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Sorting using lambda
students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda student: student[1], reverse=True)
print(students)  # Output: [('Alice', 90), ('Charlie', 85), ('Bob', 75)]
```

---

## Common Mistakes

### Mutable Default Arguments
A common Python trap is using a mutable object (like a list or dictionary) as a default parameter value. Python evaluates the default value only **once** when the function is defined, meaning the same object is shared across all function calls.

```python
# Incorrect:
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [1, 2] -- 1 is still there!

# Correct:
def add_item_correct(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_correct(1))  # Output: [1]
print(add_item_correct(2))  # Output: [2]
```

---

## Further Reading

- [Official Python Docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Official Python Docs — More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
