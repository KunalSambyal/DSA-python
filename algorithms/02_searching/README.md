# Searching Algorithms

Searching is the process of finding the position of a target element within a data structure. This directory focuses on efficient search techniques in Python and C++.

---

## Comparison Table

| Algorithm                     | Best Case | Average Case | Worst Case   | Space Complexity | Prerequisites        | Description                                        |
| :---------------------------- | :-------- | :----------- | :----------- | :--------------- | :------------------- | :------------------------------------------------- |
| **Linear Search**             | **O(1)**  | **O(N)**     | **O(N)**     | **O(1)**         | None                 | Scan elements sequentially one by one.             |
| **Binary Search (Iterative)** | **O(1)**  | **O(log N)** | **O(log N)** | **O(1)**         | Array must be sorted | Halve the search space repeatedly using a loop.    |
| **Binary Search (Recursive)** | **O(1)**  | **O(log N)** | **O(log N)** | **O(log N)**     | Array must be sorted | Halve the search space repeatedly using recursion. |

---

## Detailed Explanations

### 1. Linear Search

**Condition:** None (works on both sorted and unsorted collections).

#### Algorithm

1. Start from the first element of the array.
2. Compare the current element with the target element.
3. If the current element matches the target, return its index.
4. Otherwise, advance to the next element.
5. Repeat until the target is found or the end of the array is reached.
6. If the target element is not found, return -1.

#### Pseudocode

```text
LINEAR_SEARCH(A, N, ITEM)
1. For i = 0 to N - 1
       If A[i] == ITEM
           Return i
2. Return -1
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(1)** (target is the first element).
    - **Average Case:** **O(N)**.
    - **Worst Case:** **O(N)** (target is at the end or absent).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int linearSearch(const std::vector<int>& arr, int target) {
    for (int i = 0; i < static_cast<int>(arr.size()); ++i) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
```

</details>

- **Standalone Executables:** [Python Implementation](linear_search.py) | [C++ Implementation](linear_search.cpp)

---

### 2. Binary Search (Iterative)

**Condition:** Array must be sorted in ascending order.

#### Algorithm

1. Initialize `LOW` to index 0 and `HIGH` to index `N - 1`.
2. While `LOW <= HIGH`:
    - Calculate the midpoint index `MID = LOW + (HIGH - LOW) / 2`.
    - Compare the element at `MID` with the target element.
    - If `A[MID] == ITEM`, return `MID`.
    - If `ITEM < A[MID]`, narrow the search to the left half by setting `HIGH = MID - 1`.
    - Otherwise, narrow the search to the right half by setting `LOW = MID + 1`.
3. If `LOW > HIGH` without finding the target, return -1.

#### Pseudocode

```text
BINARY_SEARCH(A, N, ITEM)
1. LOW = 0
2. HIGH = N - 1
3. While LOW <= HIGH
       MID = LOW + (HIGH - LOW) / 2
       If A[MID] == ITEM
           Return MID
       Else if ITEM < A[MID]
           HIGH = MID - 1
       Else
           LOW = MID + 1
4. Return -1
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(1)** (target is at the middle element on first probe).
    - **Average Case:** **O(log N)**.
    - **Worst Case:** **O(log N)**.
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def binary_search_iterative(arr, target):
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

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int binarySearchIterative(const std::vector<int>& arr, int target) {
    int low = 0;
    int high = static_cast<int>(arr.size()) - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;
}
```

</details>

- **Standalone Executables:** [Python Implementation](binary_search.py) | [C++ Implementation](binary_search.cpp)

---

### 3. Binary Search (Recursive)

**Condition:** Array must be sorted in ascending order.

#### Algorithm

1. Base case: If `LOW > HIGH`, the search space is exhausted; return -1.
2. Calculate the midpoint index `MID = LOW + (HIGH - LOW) / 2`.
3. If `A[MID] == ITEM`, return `MID`.
4. If `ITEM < A[MID]`, recursively search the left sub-array from `LOW` to `MID - 1`.
5. Otherwise, recursively search the right sub-array from `MID + 1` to `HIGH`.

#### Pseudocode

```text
BINARY_SEARCH_RECURSIVE(A, ITEM, LOW, HIGH)
1. If LOW > HIGH
       Return -1
2. MID = LOW + (HIGH - LOW) / 2
3. If A[MID] == ITEM
       Return MID
4. Else if ITEM < A[MID]
       Return BINARY_SEARCH_RECURSIVE(A, ITEM, LOW, MID - 1)
5. Else
       Return BINARY_SEARCH_RECURSIVE(A, ITEM, MID + 1, HIGH)
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(1)** (target is at the midpoint on the first call).
    - **Average Case:** **O(log N)**.
    - **Worst Case:** **O(log N)**.
- **Space Complexity:** **O(log N)** auxiliary space on the recursive call stack.

<details>
<summary><b>Python Implementation</b></summary>

```python
def binary_search_recursive_helper(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive_helper(arr, target, mid + 1, high)
    else:
        return binary_search_recursive_helper(arr, target, low, mid - 1)

def binary_search_recursive(arr, target):
    return binary_search_recursive_helper(arr, target, 0, len(arr) - 1)
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int binarySearchRecursiveHelper(const std::vector<int>& arr, int target, int low, int high) {
    if (low > high) {
        return -1;
    }

    int mid = low + (high - low) / 2;
    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursiveHelper(arr, target, mid + 1, high);
    } else {
        return binarySearchRecursiveHelper(arr, target, low, mid - 1);
    }
}

int binarySearchRecursive(const std::vector<int>& arr, int target) {
    return binarySearchRecursiveHelper(arr, target, 0, static_cast<int>(arr.size()) - 1);
}
```

</details>

- **Standalone Executables:** [Python Implementation](binary_search.py) | [C++ Implementation](binary_search.cpp)
