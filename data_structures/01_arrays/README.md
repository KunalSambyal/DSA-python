# Arrays and Dynamic Arrays

In computer science, **arrays** are fundamental linear data structures that store elements in contiguous memory locations. They allow constant-time indexed access, making them one of the most widely used building blocks in software design and algorithmic problem solving.

---

## 1. Concept & Explanation

### Fixed vs. Dynamic Arrays

- **Fixed Arrays**: Traditional static arrays have a fixed size allocated at creation time. Once full, their capacity cannot be expanded without allocating a new array and copying the elements.
- **Dynamic Arrays**: Dynamic arrays automatically resize themselves when their capacity limit is reached. They manage internal buffers with extra capacity to minimize expensive reallocation and copying steps.

### Language Representations

- **Python (`list`)**:
    - Python implements dynamic arrays via its built-in `list` type.
    - Internally, a Python list stores a contiguous block of memory containing pointers (references) to the actual Python objects (`PyObject*`).
    - When the list runs out of allocated slots, Python reallocates a larger memory buffer using a dynamic growth formula (roughly 1.125x growth factor) and copies existing references over.

- **C++ (`std::vector`)**:
    - C++ implements dynamic arrays through the Standard Template Library (STL) container `std::vector<T>`.
    - Unlike Python lists, `std::vector` stores elements inline and contiguously by value in heap memory (unless pointers are explicitly stored), providing exceptional cache locality.
    - When capacity is exceeded, `std::vector` typically allocates a new buffer with double the previous capacity (2x or 1.5x depending on compiler/standard library implementation) and moves or copies elements.

For complete runnable scripts, see:

- [arrays.py](arrays.py) (Python implementation)
- [arrays.cpp](arrays.cpp) (C++ implementation)

---

## 2. Complexity Analysis

| Operation                  | Time Complexity (Average) | Time Complexity (Worst Case) | Space Complexity | Description                                                    |
| :------------------------- | :------------------------ | :--------------------------- | :--------------- | :------------------------------------------------------------- |
| **Index Access / Update**  | **O(1)**                  | **O(1)**                     | **O(1)**         | Direct memory offset calculation via `arr[i]`.                 |
| **Search (Unsorted)**      | **O(N)**                  | **O(N)**                     | **O(1)**         | Sequential scanning from start to end.                         |
| **Search (Sorted)**        | **O(log N)**              | **O(log N)**                 | **O(1)**         | Binary search on a pre-sorted array.                           |
| **Insert at End (Append)** | **O(1)** (amortized)      | **O(N)**                     | **O(1)**         | Adding to the end; **O(N)** worst case occurs during resize.   |
| **Insert at Start**        | **O(N)**                  | **O(N)**                     | **O(1)**         | Shifts all existing elements one position to the right.        |
| **Insert at Index**        | **O(N)**                  | **O(N)**                     | **O(1)**         | Shifts subsequent elements from the target index to the right. |
| **Delete from End (Pop)**  | **O(1)**                  | **O(1)**                     | **O(1)**         | Removing the last element directly without shifting.           |
| **Delete from Start**      | **O(N)**                  | **O(N)**                     | **O(1)**         | Shifts all remaining elements one position to the left.        |
| **Delete by Index**        | **O(N)**                  | **O(N)**                     | **O(1)**         | Shifts subsequent elements to the left to close the gap.       |
| **Traversal**              | **O(N)**                  | **O(N)**                     | **O(1)**         | Visiting and processing each element sequentially.             |
| **In-place Reversal**      | **O(N)**                  | **O(N)**                     | **O(1)**         | Two-pointer swap approach from both ends moving inward.        |

> **Amortized Analysis of Append:** When capacity is exceeded, an array resize requires allocating a new memory block and copying all **N** elements, which takes **O(N)** time. However, because capacity grows geometrically (e.g., doubling), resizes happen infrequently. The cost of copying is distributed across the preceding **O(N)** appends, guaranteeing an average amortized time complexity of **O(1)** per append.

---

## 3. Basic Algorithms & Core Operations

### Elementary Operations

#### 1. Insert at Beginning (Prepend)

**Condition:** Dynamic array must have capacity or resize capability.

##### Algorithm

1. Check if the array has sufficient capacity; if full, resize by allocating a larger buffer.
2. Shift every element from index 0 to `N - 1` one position to the right (from right to left).
3. Place the new element at index 0.
4. Increment the array size counter by one.

##### Pseudocode

```text
INSERT_AT_START(A, N, ITEM)
1. For i = N - 1 down to 0
       A[i + 1] = A[i]
2. A[0] = ITEM
3. N = N + 1
4. Return A
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(N)**, Worst Case: **O(N)** (all N elements must shift).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def insert_at_start(arr, element):
    arr.insert(0, element)
    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void insertAtStart(std::vector<int>& arr, int element) {
    arr.insert(arr.begin(), element);
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 2. Insert at End (Append)

**Condition:** Dynamic array must have capacity or resize capability.

##### Algorithm

1. Check whether internal buffer capacity is full.
2. If full, allocate a new larger memory block, copy existing elements, and update capacity.
3. Assign the new element at index `N`.
4. Increment the size counter by one.

##### Pseudocode

```text
INSERT_AT_END(A, N, ITEM)
1. If N == CAPACITY
       RESIZE(A)
2. A[N] = ITEM
3. N = N + 1
4. Return A
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(1)**, Average Case: **O(1)** (amortized), Worst Case: **O(N)** (when reallocation occurs).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def insert_at_end(arr, element):
    arr.append(element)
    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void insertAtEnd(std::vector<int>& arr, int element) {
    arr.push_back(element);
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 3. Insert at Arbitrary Index

**Condition:** Target index must satisfy `0 <= INDEX <= N`.

##### Algorithm

1. Verify that `INDEX` is within valid insertion bounds (`0 <= INDEX <= N`).
2. If the array is full, resize the buffer.
3. Shift all elements from index `INDEX` up to `N - 1` one position to the right (iterating backward).
4. Place the new element at `A[INDEX]`.
5. Increment the array size counter by one.

##### Pseudocode

```text
INSERT_AT_INDEX(A, N, INDEX, ITEM)
1. If INDEX < 0 or INDEX > N
       Report "Index Out of Bounds"
       Return
2. For i = N - 1 down to INDEX
       A[i + 1] = A[i]
3. A[INDEX] = ITEM
4. N = N + 1
5. Return A
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(1)** (when inserting at end), Worst Case: **O(N)** (when inserting near beginning).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def insert_at_index(arr, index, element):
    if index < 0 or index > len(arr):
        raise IndexError("Index out of bounds")
    arr.insert(index, element)
    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void insertAtIndex(std::vector<int>& arr, int index, int element) {
    if (index < 0 || index > static_cast<int>(arr.size())) {
        throw std::out_of_range("Index out of bounds");
    }
    arr.insert(arr.begin() + index, element);
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 4. Delete from Beginning (Pop First)

**Condition:** Array must not be empty (`N > 0`).

##### Algorithm

1. Check if the array is empty (`N == 0`); if so, report underflow.
2. Store the first element `A[0]` in a temporary variable.
3. Shift each subsequent element from index 1 to `N - 1` one position to the left.
4. Decrement the array size counter by one.
5. Return the stored first element.

##### Pseudocode

```text
DELETE_FROM_START(A, N)
1. If N == 0
       Report "Array Underflow"
       Return
2. ITEM = A[0]
3. For i = 0 to N - 2
       A[i] = A[i + 1]
4. N = N - 1
5. Return ITEM
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(N)**, Worst Case: **O(N)** (all remaining elements must shift left).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def delete_from_start(arr):
    if not arr:
        raise IndexError("Cannot delete from an empty array")
    return arr.pop(0)
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int deleteFromStart(std::vector<int>& arr) {
    if (arr.empty()) {
        throw std::out_of_range("Cannot delete from an empty array");
    }
    int firstVal = arr.front();
    arr.erase(arr.begin());
    return firstVal;
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 5. Delete from End (Pop)

**Condition:** Array must not be empty (`N > 0`).

##### Algorithm

1. Check if the array is empty (`N == 0`); if so, report underflow.
2. Retrieve the element at index `N - 1`.
3. Decrement the array size counter by one.
4. Return the removed element.

##### Pseudocode

```text
DELETE_FROM_END(A, N)
1. If N == 0
       Report "Array Underflow"
       Return
2. ITEM = A[N - 1]
3. N = N - 1
4. Return ITEM
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(1)**, Worst Case: **O(1)** (no element shifting required).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def delete_from_end(arr):
    if not arr:
        raise IndexError("Cannot delete from an empty array")
    return arr.pop()
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int deleteFromEnd(std::vector<int>& arr) {
    if (arr.empty()) {
        throw std::out_of_range("Cannot delete from an empty array");
    }
    int lastVal = arr.back();
    arr.pop_back();
    return lastVal;
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 6. Delete by Index

**Condition:** Target index must satisfy `0 <= INDEX < N`.

##### Algorithm

1. Verify that `INDEX` is valid (`0 <= INDEX < N`); if not, report out of bounds.
2. Store the element at `A[INDEX]`.
3. Shift all elements from index `INDEX + 1` up to `N - 1` one position to the left.
4. Decrement the array size counter by one.
5. Return the stored element.

##### Pseudocode

```text
DELETE_BY_INDEX(A, N, INDEX)
1. If INDEX < 0 or INDEX >= N
       Report "Index Out of Bounds"
       Return
2. ITEM = A[INDEX]
3. For i = INDEX to N - 2
       A[i] = A[i + 1]
4. N = N - 1
5. Return ITEM
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(1)** (deleting from end), Worst Case: **O(N)** (deleting from start).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def delete_by_index(arr, index):
    if index < 0 or index >= len(arr):
        raise IndexError("Index out of bounds")
    return arr.pop(index)
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int deleteByIndex(std::vector<int>& arr, int index) {
    if (index < 0 || index >= static_cast<int>(arr.size())) {
        throw std::out_of_range("Index out of bounds");
    }
    int val = arr[index];
    arr.erase(arr.begin() + index);
    return val;
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 7. Traversal and Display

**Condition:** None.

##### Algorithm

1. Start from index 0.
2. Iterate sequentially through each index up to `N - 1`.
3. Read, process, or print each element `A[i]`.
4. Terminate when index reaches `N`.

##### Pseudocode

```text
TRAVERSE_ARRAY(A, N)
1. For i = 0 to N - 1
       Print "Index", i, "->", A[i]
2. Return
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(N)**, Worst Case: **O(N)**.
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def traverse_array(arr):
    for idx, val in enumerate(arr):
        print(f"Index {idx} -> {val}")
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void traverseArray(const std::vector<int>& arr) {
    for (int i = 0; i < static_cast<int>(arr.size()); ++i) {
        std::cout << "Index " << i << " -> " << arr[i] << "\n";
    }
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

### Standard Array Algorithms

#### 8. Finding the Minimum / Maximum Value

**Condition:** Array must contain at least one element (`N >= 1`).

##### Algorithm

1. Check if the array is empty; if so, report error.
2. Initialize `MIN_VAL` to the first element `A[0]`.
3. Iterate through each element from index 1 to `N - 1`.
4. If the current element is smaller than `MIN_VAL`, update `MIN_VAL = A[i]`.
5. Return `MIN_VAL` after inspecting all elements.

##### Pseudocode

```text
FIND_MINIMUM(A, N)
1. If N == 0
       Report "Array is Empty"
       Return
2. MIN_VAL = A[0]
3. For i = 1 to N - 1
       If A[i] < MIN_VAL
           MIN_VAL = A[i]
4. Return MIN_VAL
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(N)**, Worst Case: **O(N)** (every element must be examined).
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def find_minimum(arr):
    if not arr:
        raise ValueError("Array is empty")
    min_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
    return min_val
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int findMinimum(const std::vector<int>& arr) {
    if (arr.empty()) {
        throw std::invalid_argument("Array is empty");
    }
    int minVal = arr[0];
    for (int num : arr) {
        if (num < minVal) {
            minVal = num;
        }
    }
    return minVal;
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 9. Linear Search

**Condition:** None (works on unsorted or sorted arrays).

##### Algorithm

1. Start from the first element at index 0.
2. Compare each element sequentially with the target item.
3. If a match is found, return the current index.
4. If the end of the array is reached without a match, return -1.

##### Pseudocode

```text
LINEAR_SEARCH(A, N, ITEM)
1. For i = 0 to N - 1
       If A[i] == ITEM
           Return i
2. Return -1
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(1)**, Average Case: **O(N)**, Worst Case: **O(N)**.
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

```python
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
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

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 10. Binary Search

**Condition:** Array must be sorted in ascending order.

##### Algorithm

1. Initialize `LOW` to 0 and `HIGH` to `N - 1`.
2. While `LOW <= HIGH`:
    - Compute midpoint index `MID = LOW + (HIGH - LOW) / 2`.
    - If `A[MID] == ITEM`, return `MID`.
    - If `ITEM < A[MID]`, eliminate the right half by setting `HIGH = MID - 1`.
    - Otherwise, eliminate the left half by setting `LOW = MID + 1`.
3. If search space is exhausted without a match, return -1.

##### Pseudocode

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

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(1)**, Average Case: **O(log N)**, Worst Case: **O(log N)**.
- **Space Complexity:** **O(1)** auxiliary space.

<details>
<summary><b>Python Implementation</b></summary>

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

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int binarySearch(const std::vector<int>& arr, int target) {
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

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

#### 11. Reversing an Array (In-Place)

**Condition:** None.

##### Algorithm

1. Initialize two pointers: `LEFT = 0` and `RIGHT = N - 1`.
2. While `LEFT < RIGHT`:
    - Swap the values at `A[LEFT]` and `A[RIGHT]`.
    - Increment `LEFT` by one.
    - Decrement `RIGHT` by one.
3. Terminate when `LEFT >= RIGHT`.

##### Pseudocode

```text
REVERSE_ARRAY(A, N)
1. LEFT = 0
2. RIGHT = N - 1
3. While LEFT < RIGHT
       TEMP = A[LEFT]
       A[LEFT] = A[RIGHT]
       A[RIGHT] = TEMP
       LEFT = LEFT + 1
       RIGHT = RIGHT - 1
4. Return A
```

##### Complexity Analysis

- **Time Complexity:** Best Case: **O(N)**, Worst Case: **O(N)** (requires N/2 swaps).
- **Space Complexity:** **O(1)** auxiliary space (in-place modification).

<details>
<summary><b>Python Implementation</b></summary>

```python
def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void reverseArrayInPlace(std::vector<int>& arr) {
    int left = 0;
    int right = static_cast<int>(arr.size()) - 1;

    while (left < right) {
        std::swap(arr[left], arr[right]);
        ++left;
        --right;
    }
}
```

</details>

- **Standalone Executables:** [Python Implementation](arrays.py) | [C++ Implementation](arrays.cpp)

---

## 4. Related Resources

- **Python Implementation**: [arrays.py](arrays.py)
- **C++ Implementation**: [arrays.cpp](arrays.cpp)
- **Parent Directory**: [data_structures README](../README.md)
