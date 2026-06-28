# Exception Handling

An exception is an error that occurs during the execution of a program. When an error occurs, Python stops and generates an error message. You can handle exceptions using `try`, `except`, `else`, and `finally` blocks to keep the program running.

---

## 1. The `try-except` Block

* **`try` block**: Tests a block of code for errors.
* **`except` block**: Handles the error if one occurs.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

### Catching Multiple Exceptions in One Line
You can catch different exceptions together using parentheses.

```python
try:
    value = int("abc")
except (TypeError, ValueError) as e:
    print(f"Caught an error: {e}")
```

### The `as` Keyword
Use the `as` keyword to inspect the exception object and print its details.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error details: {e}")  # Output: Error details: division by zero
```

---

## 2. The `else` and `finally` Keywords

* **`else`**: Runs code if no exception occurred in the `try` block.
* **`finally`**: Always runs regardless of whether an exception was raised.

```python
try:
    print("Running process...")
except ZeroDivisionError:
    print("Error occurred")
else:
    print("Process succeeded with no errors!")
finally:
    print("Cleaning up resources.")  # This will run no matter what
```

---

## 3. Raising Custom Exceptions

You can manually trigger exceptions using the `raise` keyword. You can also create custom exception classes by inheriting from the built-in `Exception` class.

```python
# Custom exception class
class InsufficientFundsError(Exception):
    """Raised when a bank withdrawal exceeds the available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Balance is only {balance}.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(e)  # Output: Cannot withdraw 200. Balance is only 100.
```

---

## 4. Common Built-in Exceptions Reference

| Exception | When it occurs |
|---|---|
| `ValueError` | Right type but wrong value (e.g., `int("abc")`). |
| `TypeError` | Operation on incompatible types (e.g., `"a" + 1`). |
| `IndexError` | Accessing a sequence index that doesn't exist. |
| `KeyError` | Accessing a dictionary key that doesn't exist. |
| `ZeroDivisionError` | Dividing a number by zero. |
| `FileNotFoundError` | Trying to open a file that does not exist. |
| `AttributeError` | Accessing an attribute that doesn't exist on an object. |
| `ImportError` | Importing a module that doesn't exist. |

---

## Common Mistakes

### Using a Bare `except:`
Using `except:` without specifying an exception class catches *all* exceptions, including system-exiting exceptions like `SystemExit` and `KeyboardInterrupt` (when you try to stop execution using Ctrl+C). This makes debugging extremely hard.

```python
# Incorrect:
try:
    # Some code
    pass
except:
    print("An error occurred")  # Catches EVERYTHING, even system interrupts!

# Correct:
try:
    # Some code
    pass
except Exception as e:
    print(f"An unexpected error occurred: {e}")  # Catches standard exceptions only
```

---

## Further Reading

- [Official Python Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Official Python Docs — Built-in Exceptions Reference](https://docs.python.org/3/library/exceptions.html)
