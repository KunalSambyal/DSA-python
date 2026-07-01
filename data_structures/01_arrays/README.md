# Lists and Arrays in Python

In computer science, **arrays** are fundamental contiguous-memory linear data structures. In Python, the built-in `list` data type serves as the standard dynamic array.

For practical examples, see the reference script: [arrays.py](arrays.py).

---

## Time and Space Complexity

The table below summarizes the time and space complexity of common dynamic array operations in Python:

| Operation                 | Time Complexity (Average) | Time Complexity (Worst Case) | Space Complexity | Description                                                    |
| :------------------------ | :------------------------ | :--------------------------- | :--------------- | :------------------------------------------------------------- |
| **Index Access**          | **O(1)**                  | **O(1)**                     | **O(1)**         | Accessing or editing an item at index i via `arr[i]`           |
| **Search (Unsorted)**     | **O(N)**                  | **O(N)**                     | **O(1)**         | Scanning sequentially via `in` or `index()`                    |
| **Search (Sorted)**       | **O(log N)**              | **O(log N)**                 | **O(1)**         | Using Binary Search on a pre-sorted list                       |
| **Append**                | **O(1)** (amortized)      | **O(N)**                     | **O(1)**         | Adding an element to the end of the list                       |
| **Insert / Pop (Middle)** | **O(N)**                  | **O(N)**                     | **O(1)**         | Shifting subsequent elements (e.g., `insert(0, x)`, `pop(i)`)  |
| **Delete (by value)**     | **O(N)**                  | **O(N)**                     | **O(1)**         | Finding first match and shifting remaining items (`remove()`)  |
| **Slicing / Copying**     | **O(K)**                  | **O(K)**                     | **O(K)**         | Copying K elements to construct a new list (`arr[start:stop]`) |
| **Sort**                  | **O(N)**                  | **O(N)**                     | **O(N)**         | Timsort algorithm (built-in `.sort()` and `sorted()`)          |

> **Amortized O(1) Append:** Python lists pre-allocate extra memory capacity. When the capacity is exceeded, Python allocates a new larger memory block and copies the elements over. The reallocation cost is spread across many appends, resulting in an average **O(1)** time complexity per append.

---

## Basic Algorithms on Arrays

### 1. Finding the Minimum/Maximum Value

To find the lowest or highest value in a list, we traverse every item exactly once.

- **Time Complexity:** **O(N)**
- **Space Complexity:** **O(1)**

```python
def find_minimum(arr):
    if not arr:
        raise ValueError("Array is empty")
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val
```

### 2. Linear Search

Check each item sequentially until a match is found.

- **Time Complexity:** **O(N)**
- **Space Complexity:** **O(1)**

```python
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i  # Return index of found element
    return -1  # Target not found
```

### 3. Binary Search (Requires a Sorted Array)

Repeatedly divide the search interval in half.

- **Time Complexity:** **O(log N)**
- **Space Complexity:** **O(1)**

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### 4. Reversing an Array

Swap elements from both ends moving towards the middle.

- **Time Complexity:** **O(N)**
- **Space Complexity:** **O(1)** (in-place)

```python
def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

---

## Related Resources

- Check out the full implementation and code examples in [arrays.py](arrays.py).
- For overall data structure details, refer to the parent directory [data_structures README](../README.md).
