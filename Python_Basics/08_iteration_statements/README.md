# Iteration Statements (Loops)

Iteration statements, or loops, are used to execute a block of code repeatedly as long as a condition is met or for a sequence of elements.

Python has two primitive loop commands:

## 1. The `while` Loop

A `while` loop executes a block of code as long as a specified condition remains `True`.

### Example

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

*Note: Remember to increment the counter variable (`count` in this case), otherwise the loop will run forever (an infinite loop).*

---

## 2. The `for` Loop

A `for` loop is used for iterating over a sequence (such as a list, a tuple, a dictionary, a set, or a string).

### Example: Iterating over a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Example: Using the `range()` function

To loop through a set of code a specified number of times, we can use the `range()` function. It returns a sequence of numbers, starting from 0 by default, and increments by 1 by default, ending before the specified number.

```python
for i in range(5):
    print(i)  # Prints numbers from 0 to 4
```

---

## Loop Control Statements

You can control how loops run using the following keywords:

### `break`

The `break` statement is used to terminate the loop immediately.

```python
for x in range(10):
    if x == 3:
        break
    print(x)  # Prints 0, 1, 2
```

### `continue`

The `continue` statement stops the current iteration of the loop, and continues with the next iteration.

```python
for x in range(5):
    if x == 2:
        continue
    print(x)  # Prints 0, 1, 3, 4 (skips 2)
```
