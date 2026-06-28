# Conditional Statements

Conditional statements allow your program to make decisions and run different blocks of code depending on whether a condition is true or false.

Python supports the usual logical conditions from mathematics:
* Equal to: `a == b`
* Not Equal to: `a != b`
* Less than: `a < b`
* Less than or equal to: `a <= b`
* Greater than: `a > b`
* Greater than or equal to: `a >= b`

## `if` Statement

The `if` statement executes a block of code if the specified condition evaluates to `True`.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## `elif` Statement

The `elif` keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

```python
x = 5
if x > 10:
    print("x is greater than 10")
elif x > 2:
    print("x is greater than 2 but not greater than 10")
```

## `else` Statement

The `else` keyword catches anything which wasn't caught by the preceding conditions.

```python
x = 1
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

## Nested `if` Statements

You can have `if` statements inside `if` statements. This is called nested `if` statements.

```python
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```
