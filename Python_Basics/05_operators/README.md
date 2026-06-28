# Operators

Operators are used to perform operations on variables and values. Python divides operators into several groups.

## 1. Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name | Example | Result (if x = 10, y = 3) |
|---|---|---|---|
| `+` | Addition | `x + y` | `13` |
| `-` | Subtraction | `x - y` | `7` |
| `*` | Multiplication | `x * y` | `30` |
| `/` | Division | `x / y` | `3.3333333333333335` |
| `%` | Modulus (Remainder) | `x % y` | `1` |
| `**` | Exponentiation (Power) | `x ** y` | `1000` |
| `//` | Floor Division (Integer Division) | `x // y` | `3` |

## 2. Assignment Operators

Assignment operators are used to assign values to variables:

* **`=`**: `x = 5` (assigns 5 to x)
* **`+=`**: `x += 3` (equivalent to `x = x + 3`)
* **`-=`**: `x -= 3` (equivalent to `x = x - 3`)
* **`*=`**: `x *= 3` (equivalent to `x = x * 3`)

## 3. Comparison Operators

Comparison operators are used to compare two values, returning `True` or `False`:

* **`==`**: Equal (e.g., `x == y`)
* **`!=`**: Not equal (e.g., `x != y`)
* **`>`**: Greater than (e.g., `x > y`)
* **`<`**: Less than (e.g., `x < y`)
* **`>=`**: Greater than or equal to (e.g., `x >= y`)
* **`<=`**: Less than or equal to (e.g., `x <= y`)

## 4. Logical Operators

Logical operators are used to combine conditional statements:

* **`and`**: Returns `True` if both statements are true (e.g., `x > 5 and x < 15`)
* **`or`**: Returns `True` if at least one statement is true (e.g., `x > 5 or x < 2`)
* **`not`**: Reverses the result, returning `False` if the result is true (e.g., `not(x > 5)`)

## 5. Membership Operators

Membership operators are used to test if a sequence is present in an object:

* **`in`**: Returns `True` if a sequence with the specified value is present in the object (e.g., `'a' in 'apple'`).
* **`not in`**: Returns `True` if a sequence with the specified value is not present in the object (e.g., `'b' not in 'apple'`).
