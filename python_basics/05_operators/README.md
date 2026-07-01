# Operators

Operators are used to perform operations on variables and values. Python divides operators into several groups.

---

## 1. Arithmetic Operators

Arithmetic operators are used with numeric values to perform mathematical operations:

| Operator | Name           | Example  | Result (if x = 10, y = 3) |
| -------- | -------------- | -------- | ------------------------- |
| `+`      | Addition       | `x + y`  | `13`                      |
| `-`      | Subtraction    | `x - y`  | `7`                       |
| `*`      | Multiplication | `x * y`  | `30`                      |
| `/`      | Division       | `x / y`  | `3.3333333333333335`      |
| `%`      | Modulus        | `x % y`  | `1`                       |
| `**`     | Exponentiation | `x ** y` | `1000`                    |
| `//`     | Floor Division | `x // y` | `3`                       |

---

## 2. Assignment Operators

Assignment operators are used to assign values to variables:

| Operator | Example   | Same As      |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | `x = 5`      |
| `+=`     | `x += 3`  | `x = x + 3`  |
| `-=`     | `x -= 3`  | `x = x - 3`  |
| `*=`     | `x *= 3`  | `x = x * 3`  |
| `/=`     | `x /= 3`  | `x = x / 3`  |
| `//=`    | `x //= 3` | `x = x // 3` |
| `**=`    | `x **= 3` | `x = x ** 3` |
| `%=`     | `x %= 3`  | `x = x % 3`  |

---

## 3. Comparison Operators

Comparison operators are used to compare two values, returning `True` or `False`:

- `==` : Equal
- `!=` : Not equal
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

---

## 4. Logical Operators

Logical operators are used to combine conditional statements:

- **`and`**: Returns `True` if both statements are true (e.g., `x > 5 and x < 15`).
- **`or`**: Returns `True` if at least one statement is true (e.g., `x > 5 or x < 2`).
- **`not`**: Reverses the result (e.g., `not(x > 5)`).

---

## 5. Identity Operators

Identity operators compare the memory locations of two objects to see if they are the exact same instance in memory.

- **`is`**: Returns `True` if both variables point to the same object.
- **`is not`**: Returns `True` if both variables point to different objects.

```python
a = [1, 2, 3]
b = a          # b points to the same list object
c = [1, 2, 3]  # c is a new list object with the same values

print(a == c)  # Output: True  (same values)
print(a is c)  # Output: False (different objects in memory)
print(a is b)  # Output: True  (same object in memory)
```

---

## 6. Membership Operators

Membership operators are used to test if a sequence (like a string, list, or tuple) is present in an object:

- **`in`**: Returns `True` if the value is found.
- **`not in`**: Returns `True` if the value is not found.

```python
fruits = ["apple", "banana"]
print("apple" in fruits)      # Output: True
print("cherry" not in fruits)  # Output: True
```

---

## 7. Bitwise Operators

Bitwise operators are used to perform bitwise calculations on integers by converting them to binary:

- `&` (AND): Sets each bit to 1 if both bits are 1.
- `|` (OR): Sets each bit to 1 if one of two bits is 1.
- `^` (XOR): Sets each bit to 1 if only one of two bits is 1.
- `~` (NOT): Inverts all the bits.
- `<<` (Zero fill left shift): Shift left by pushing zeros in from the right.
- `>>` (Signed right shift): Shift right by pushing copies of the leftmost bit in from the left.

---

## 8. The Walrus Operator (`:=`)

Introduced in Python 3.8, the assignment expression operator (known as the walrus operator) allows you to assign values to a variable inside an expression.

```python
numbers = [1, 2, 3, 4, 5, 6]
if (n := len(numbers)) > 4:
    print(f"List is too long ({n} elements)")  # Output: List is too long (6 elements)
```

---

## Common Mistakes

### Using `is` to compare values instead of `==`

The `is` operator checks if two references point to the exact same object in memory, while `==` checks if they have the same value. Using `is` for value comparison (such as with integers or strings) can lead to unexpected bugs because Python optimizes small objects but creates new objects for larger ones.

```python
a = 1000
b = 1000
print(a == b)  # Output: True (values are equal)
print(a is b)  # Output: False (different objects in memory)
```

---

## Further Reading

- [Official Python Docs — Expressions](https://docs.python.org/3/reference/expressions.html)
- [Official Python Docs — Operators](https://docs.python.org/3/library/stdtypes.html#special-attributes)
