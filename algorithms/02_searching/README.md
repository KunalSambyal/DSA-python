# Searching Algorithms

Searching is the process of finding the position of a target element within a data structure. This directory focuses on efficient search techniques.

---

## Comparison Table

| Algorithm                     | Best Case | Average Case | Worst Case   | Space Complexity | Prerequisites        | Description                                        |
| :---------------------------- | :-------- | :----------- | :----------- | :--------------- | :------------------- | :------------------------------------------------- |
| **Linear Search**             | **O(1)**  | **O(N)**     | **O(N)**     | **O(1)**         | None                 | Scan elements sequentially one by one.             |
| **Binary Search (Iterative)** | **O(1)**  | **O(log N)** | **O(log N)** | **O(1)**         | Array must be sorted | Halve the search space repeatedly using a loop.    |
| **Binary Search (Recursive)** | **O(1)**  | **O(log N)** | **O(log N)** | **O(log N)**     | Array must be sorted | Halve the search space repeatedly using recursion. |

---

## Detailed Explanations

### Linear Search

- **File:** [linear_search.py](linear_search.py)
- **Concept:** Sequentially scans each element of the collection from the beginning until a match is found or the end of the collection is reached.
- **Prerequisite:** None. Works on both sorted and unsorted collections.
- **Space Complexity:** **O(1)** auxiliary space.

### Binary Search

- **File:** [binary_search.py](binary_search.py)
- **Concept:** Works on a sorted array by repeatedly dividing the search interval in half. Compare the target value to the middle element of the array. If they are unequal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half.
- **Prerequisite:** The input array **must** be sorted. If it is unsorted, Binary Search will yield incorrect results.

#### 1. Iterative Approach

- **Implementation:** Uses a `while` loop with `low` and `high` index pointers.
- **Space Complexity:** **O(1)** auxiliary space, as it only requires a few variables.

#### 2. Recursive Approach

- **Implementation:** Recursively calls the search helper function on the sub-array.
- **Space Complexity:** **O(log N)** auxiliary space due to the recursive call stack.
