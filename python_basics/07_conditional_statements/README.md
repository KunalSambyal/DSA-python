# Conditional Statements

Conditional statements allow your program to make decisions and run different blocks of code depending on whether a condition is true or false.

---

## 1. `if`, `elif`, and `else`

* **`if`**: Executes code if the condition is `True`.
* **`elif`** (else if): Checks another condition if the previous one was `False`.
* **`else`**: Catches everything not caught by preceding conditions.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

---

## 2. Nested `if` Statements

You can place `if` statements inside another `if` statement to build complex decision trees.

```python
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
```

---

## 3. Ternary (One-Line) Conditional Expressions

A ternary expression allows you to quickly evaluate a condition and assign a value on a single line.

```python
# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult
```

---

## 4. The `match` Statement (Python 3.10+)

Introduced in Python 3.10, the `match` statement provides structural pattern matching, which acts like a modern version of `switch-case` statements in other languages. The underscore `_` acts as the wildcard/default case.

```python
status_code = 404

match status_code:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")
```

---

## Common Mistakes

### Forgetting Truthy and Falsy Rules
In Python, you do not always need to check `if x == True:` or `if len(x) > 0:`. Python evaluates empty collections and zero values as `False` (Falsy) and non-empty values as `True` (Truthy).

The following values evaluate to **Falsy**:
* `None`
* `False`
* `0` (and `0.0`, `0j`)
* Empty sequences/mappings: `""`, `[]`, `()`, `{}`, `set()`

```python
# Common Beginner Mistake:
username = ""
if len(username) == 0:
    print("No username entered")

# Idiomatic Python Way:
if not username:
    print("No username entered")
```

---

## Further Reading

- [Official Python Docs — More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [PEP 636 — Structural Pattern Matching Tutorial](https://peps.python.org/pep-0636/)
