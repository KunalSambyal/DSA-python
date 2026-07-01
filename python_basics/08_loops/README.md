# Iteration Statements (Loops)

Iteration statements, or loops, are used to execute a block of code repeatedly as long as a condition is met or for a sequence of elements.

---

## 1. The `while` Loop

A `while` loop executes a block of code as long as a specified condition remains `True`.

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

---

## 2. The `for` Loop and `range()`

A `for` loop is used for iterating over a sequence (such as a list, a tuple, a dictionary, a set, or a string).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### The `range()` Function
To loop through a set of code a specified number of times, use the `range()` function. It returns a sequence of numbers, starting from 0 by default, and increments by 1 by default, ending before the specified number.

```python
for i in range(3):
    print(i)  # Prints 0, 1, 2
```

---

## 3. Loop Control Statements

* **`break`**: Terminates the loop immediately.
* **`continue`**: Stops the current iteration and jumps to the next one.
* **`pass`**: Acts as a syntactic placeholder if you do not want to run any code in the loop body.

```python
# break example
for x in range(5):
    if x == 3:
        break
    print(x)  # Prints 0, 1, 2

# continue example
for x in range(5):
    if x == 2:
        continue
    print(x)  # Prints 0, 1, 3, 4 (skips 2)
```

---

## 4. Idiomatic Looping Techniques

### Looping with Index: `enumerate()`
Instead of creating a manual counter, use `enumerate()` to retrieve both the index and the item during a loop.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

### Looping in Parallel: `zip()`
Use `zip()` to iterate over two or more sequences of the same length in parallel.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

---

## 5. Loop `else` Clause

In Python, loops can have an `else` block. The `else` block runs only if the loop completed successfully without hitting a `break` statement.

```python
for i in range(3):
    print(i)
else:
    print("Loop finished without break")  # This will print

for i in range(3):
    if i == 1:
        break
else:
    print("Loop finished")  # This will NOT print
```

---

## 6. List Comprehensions (Introductory)

A list comprehension provides a concise way to create lists using a single line of code instead of a full `for` loop.

```python
# Creating squares using list comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

---

## Further Reading

- [Official Python Docs — More Control Flow Tools (Loops)](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Official Python Docs — Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
