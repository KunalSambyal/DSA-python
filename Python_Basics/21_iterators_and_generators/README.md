# Iterators and Generators

Python handles loops and sequences under-the-hood using **Iterators**. A subclass of iterators called **Generators** provides a simple, memory-efficient way to stream large datasets without loading them entirely into memory.

---

## 1. Iterators

An **Iterator** is an object that represents a stream of data. It can be iterated over (looped through) using a `for` loop.

### How it works under the hood

An iterator must implement two methods:

1. `__iter__()`: Returns the iterator object itself.
2. `__next__()`: Returns the next item in the sequence. If there are no more items, it raises a `StopIteration` exception to terminate the loop.

```python
numbers = [1, 2]

# Get the iterator object from the list
iterator = iter(numbers)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2

# The next call raises StopIteration
# print(next(iterator))
```

---

## 2. Generators

A **Generator** is a special function that returns an iterator. Instead of returning a value and exiting like a normal function, a generator uses the `yield` statement to return a value and temporarily **pause** its execution state. When called again, it resumes right where it left off.

### Example: A simple countdown generator

```python
def countdown(n):
    while n > 0:
        yield n  # Pauses execution and returns value
        n -= 1

# Using the generator in a loop
for num in countdown(3):
    print(num)
# Output:
# 3
# 2
# 1
```

---

## 3. Why Generators? Memory Efficiency

Because generators yield items one-by-one on demand, they do not require storing the entire sequence in memory. This is highly efficient for dealing with large datasets or infinite streams.

```python
import sys

# List comprehension: builds the entire list in memory
list_result = [x ** 2 for x in range(10000)]

# Generator expression: computes values one-by-one
gen_result = (x ** 2 for x in range(10000))

print(sys.getsizeof(list_result))  # Output: ~85160 bytes
print(sys.getsizeof(gen_result))   # Output: ~104 bytes (much smaller!)
```

---

## 4. Practical Generator: Reading a Large File

When reading large logs or data files, loading the entire file into memory using `f.readlines()` can cause your program to run out of memory. Yielding line-by-line is the safest approach.

```python
def read_large_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

# Each line is yielded and processed one at a time
for line in read_large_file("huge_log.txt"):
    if "ERROR" in line:
         print(line)
```

---

## Further Reading

- [Official Python Docs — Iterators Tutorial](https://docs.python.org/3/tutorial/classes.html#iterators)
- [Official Python Docs — Generators Tutorial](https://docs.python.org/3/tutorial/classes.html#generators)
- [Official Python Docs — Yield Expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions)
