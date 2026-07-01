# Lists (Deep Dive)

A list is an ordered, mutable (changeable) collection of items. Lists are defined by placing items inside square brackets `[]` separated by commas.

---

## 1. Indexing, Slicing, and Mutability

### Indexing and Slicing
Lists use zero-based indexing, just like strings. You can slice lists to get a sublist.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])    # Output: 10
print(numbers[-1])   # Output: 50
print(numbers[1:4])  # Output: [20, 30, 40]
```

### Mutability
Unlike strings, lists are **mutable**. You can modify, add, or delete elements after creation.

```python
fruits = ["apple", "banana"]
fruits[0] = "avocado"
print(fruits)  # Output: ['avocado', 'banana']
```

---

## 2. List Methods Reference

Python provides several built-in methods to manipulate lists:

| Method | Description | Example (starting with `lst = [1, 2]`) |
|---|---|---|
| `append(x)` | Adds an item to the end of the list. | `lst.append(3)` $\rightarrow$ `[1, 2, 3]` |
| `extend(iterable)` | Appends all elements from another iterable. | `lst.extend([3, 4])` $\rightarrow$ `[1, 2, 3, 4]` |
| `insert(i, x)` | Inserts item `x` at index `i`. | `lst.insert(1, 9)` $\rightarrow$ `[1, 9, 2]` |
| `remove(x)` | Removes the first occurrence of item `x`. | `[1, 2, 1].remove(1)` $\rightarrow$ `[2, 1]` |
| `pop(i)` | Removes and returns the item at index `i` (default last item). | `lst.pop()` $\rightarrow$ returns `2`, list becomes `[1]` |
| `index(x)` | Returns the index of the first occurrence of item `x`. | `[10, 20].index(20)` $\rightarrow$ `1` |
| `count(x)` | Returns the number of times item `x` appears. | `[1, 2, 1].count(1)` $\rightarrow$ `2` |
| `sort()` | Sorts the list in-place (ascending by default). | `[2, 1].sort()` $\rightarrow$ `[1, 2]` |
| `reverse()` | Reverses the list in-place. | `[1, 2].reverse()` $\rightarrow$ `[2, 1]` |
| `copy()` | Returns a shallow copy of the list. | `lst.copy()` $\rightarrow$ independent copy of `lst` |
| `clear()` | Removes all items from the list. | `lst.clear()` $\rightarrow$ `[]` |

---

## 3. Shallow Copy vs. Deep Copy

When you assign a list to a new variable, you copy the **reference** to the list, not the actual list object. 

### Assignment Reference (Not a Copy)
```python
original = [1, 2, 3]
wrong_copy = original  # Both point to the SAME object in memory
wrong_copy.append(4)
print(original)        # Output: [1, 2, 3, 4] (original was modified!)
```

### Shallow Copy
Saves an independent copy of the list structure, but nested items are still referenced.
```python
original = [1, 2, 3]
right_copy = original.copy()  # Or: original[:]
right_copy.append(4)
print(original)               # Output: [1, 2, 3] (original remains safe)
```

### Deep Copy
If a list contains nested lists or dictionaries, changes inside the nested structure of a shallow copy will still affect the original. To create a completely independent copy of nested lists, use the `copy` module's `deepcopy()` function.
```python
import copy

nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0][0] = 99

print(nested)  # Output: [[1, 2], [3, 4]] (original is unaffected)
```

---

## 4. Built-in Functions with Lists

You can use several built-in functions to get information from lists:

```python
nums = [1, 5, 3]
print(len(nums))  # Output: 3 (length)
print(min(nums))  # Output: 1 (minimum)
print(max(nums))  # Output: 5 (maximum)
print(sum(nums))  # Output: 9 (sum)
```

---

## 5. Nested Lists

A list can contain other lists. This is often used to represent grids or matrices.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements: matrix[row][column]
print(matrix[1][2])  # Output: 6 (row index 1, column index 2)
```

---

## Further Reading

- [Official Python Docs — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Official Python Docs — Sequence Types (list)](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
