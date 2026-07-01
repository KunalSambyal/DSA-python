# Time & Space Complexity (Big-O Notation)

When writing programs, especially in technical interviews and competitive programming, we need a way to measure how efficient our algorithms are. We do this by analyzing two resources:

1. **Time Complexity:** How does the runtime scale as the size of the input grows?
2. **Space Complexity:** How much extra memory does the algorithm allocate as the size of the input grows?

We use **Big-O Notation** (written as **O(N)**) to represent the upper bound (worst-case scenario) of these complexities.

---

## The Big-O Scale (Fastest to Slowest)

Here is a quick overview of the most common complexities you will encounter, ordered from most efficient to least:

| Notation       | Name         | Visual Analogy    | Example Operation                                              |
| :------------- | :----------- | :---------------- | :------------------------------------------------------------- |
| **O(1)**       | Constant     | Instant lookup    | Reading an index in an array, hashmap lookup, basic arithmetic |
| **O(log N)**   | Logarithmic  | Dividing in half  | Binary Search, searching in a balanced Binary Search Tree      |
| **O(N)**       | Linear       | Single scan       | Linear search, iterating through a list                        |
| **O(N log N)** | Linearithmic | Divide & conquer  | Merge Sort, Quick Sort, Python's built-in `.sort()`            |
| **O(N²)**      | Quadratic    | Nested loops      | Bubble Sort, checking all pairs in a list                      |
| **O(2^N)**     | Exponential  | Tree branching    | Naive recursive Fibonacci                                      |
| **O(N!)**      | Factorial    | All possibilities | Generating all permutations of a string                        |

---

## Time Complexity with Python Examples

### 1. Constant Time: **O(1)**

The execution time of the code does not depend on the input size N. It takes the same amount of time regardless of how big the input is.

```python
def get_first_item(arr):
    return arr[0]  # O(1) time
```

### 2. Logarithmic Time: **O(log N)**

The input size is halved at each step of execution. As N grows, the number of operations grows very slowly.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # O(log N) time
```

### 3. Linear Time: **O(N)**

The execution time grows in direct proportion to the input size N.

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # Loops N times
        if num > max_val:
            max_val = num
    return max_val  # O(N) time
```

### 4. Linearithmic Time: **O(N log N)**

This complexity usually occurs when you perform a logarithmic operation N times, or in divide-and-conquer sorting algorithms.

```python
def sort_list(arr):
    return sorted(arr)  # Python uses Timsort which is O(N log N)
```

### 5. Quadratic Time: **O(N²)**

The execution time is proportional to the square of the input size N. This usually indicates nested loops.

```python
def print_all_pairs(arr):
    for i in range(len(arr)):        # Runs N times
        for j in range(len(arr)):    # Runs N times for each i
            print(arr[i], arr[j])    # O(N²) time
```

---

## Space Complexity

Space complexity measures the **additional memory (Auxiliary Space)** that an algorithm requires, relative to the input size N.

### 1. **O(1)** Space (Constant Space)

The algorithm does not allocate any new data structures whose sizes scale with N. It uses a fixed number of variables.

```python
def sum_array(arr):
    total = 0  # Fixed variable
    for num in arr:
        total += num
    return total  # O(1) auxiliary space (Input arr is not counted)
```

### 2. **O(N)** Space (Linear Space)

The algorithm creates new structures (lists, hash maps, sets) that store up to N elements.

```python
def clone_array(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)  # Appends N times
    return new_arr  # O(N) space
```

### Note on Recursion and Stack Space

Recursive calls consume space on the **Call Stack**. The depth of the recursion tree directly contributes to the space complexity.

```python
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)  # O(N) space due to N stack frames
```

---

## Rules for Analyzing Complexity

1. **Keep the Worst Case:** Big-O always measures the worst-case scenario. If a loop can terminate early, we still assume it runs to completion for Big-O.
2. **Drop Constants:** We ignore constant factors. O(2N) is simplified to O(N), and O(500) is simplified to O(1).
3. **Drop Non-Dominant Terms:** In polynomials, only keep the term with the highest growth rate. For example, O(N² + N) becomes O(N²).
4. **Multi-Part Inputs:** If an algorithm handles two different inputs of size A and B:
    - Sequential operations sum up: O(A + B)
    - Nested operations multiply: O(A × B)
