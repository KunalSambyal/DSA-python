# Input and Output

Programs interact with users by receiving input data and displaying output results.

## Output: The `print()` Function

The `print()` function is used to send data (text, numbers, etc.) to the screen.

### Basic Printing

You can print strings, numbers, or variable values. You can also print multiple items by separating them with commas (which prints a space between them by default).

```python
print("Hello, World!")
print(5 + 10)

name = "Alice"
print("Hello,", name)  # Output: Hello, Alice
```

### String Formatting (f-strings)

Formatted string literals, or **f-strings**, let you embed variables directly inside a string by prefixing the string with `f` or `F` and writing variables inside curly braces `{}`.

```python
age = 20
print(f"I am {age} years old.")  # Output: I am 20 years old.
```

---

## Input: The `input()` Function

The `input()` function allows the program to pause and wait for the user to type something. 

### Basic Input

* **Critical Note**: The `input()` function **always** returns the user's input as a string (`str`), even if they type a number.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### Reading Numbers (Type Casting)

If you want to perform math operations on the user's input, you must convert (cast) the string to a number type using `int()` or `float()`.

```python
# Reading an integer
age_input = input("Enter your age: ")
age = int(age_input)
print(f"Next year you will be {age + 1}")

# Reading a float
price = float(input("Enter item price: "))
print(f"Price with tax is {price * 1.1}")
```
