# Functions

A function is a reusable block of code that only runs when it is called. You can pass data (parameters) into a function, and a function can return data as a result.

## Defining a Function

In Python, a function is defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. The code block inside the function must be indented.

```python
def my_function():
    print("Hello from inside a function!")
```

## Calling a Function

To call a function, use the function name followed by parentheses:

```python
def my_function():
    print("Hello from inside a function!")

# Calling the function
my_function()
```

## Arguments and Parameters

Information can be passed into functions as arguments. Arguments are specified inside the parentheses in the function definition.

* **Parameter**: The variable listed inside the parentheses in the function definition.
* **Argument**: The value that is sent to the function when it is called.

### Example

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

## Return Values

To let a function return a value, use the `return` statement:

```python
def square(x):
    return x * x

result = square(4)
print(result)  # Output: 16
```
