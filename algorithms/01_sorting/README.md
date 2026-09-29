# Sorting Algorithms

Sorting is the process of arranging a collection of data in a specific order (typically ascending or descending). It is a fundamental building block in computer science, used to optimize searching, database operations, and other algorithms.

---

## Comparison Table

| Algorithm          | Best Case      | Average Case   | Worst Case     | Space Complexity | Stability | Use Case / When to Use                                                   |
| :----------------- | :------------- | :------------- | :------------- | :--------------- | :-------- | :----------------------------------------------------------------------- |
| **Bubble Sort**    | **O(N)**       | **O(N^2)**     | **O(N^2)**     | **O(1)**         | Stable    | Educational purposes; nearly sorted arrays.                              |
| **Selection Sort** | **O(N^2)**     | **O(N^2)**     | **O(N^2)**     | **O(1)**         | Unstable  | Minimize memory writes (swaps are at most **O(N)**).                     |
| **Insertion Sort** | **O(N)**       | **O(N^2)**     | **O(N^2)**     | **O(1)**         | Stable    | Small datasets or online sorting (streaming data).                       |
| **Merge Sort**     | **O(N log N)** | **O(N log N)** | **O(N log N)** | **O(N)**         | Stable    | Large datasets where stability is required (e.g., sorting linked lists). |
| **Quick Sort**     | **O(N log N)** | **O(N log N)** | **O(N^2)**     | **O(log N)**     | Unstable  | General-purpose internal sorting; fast in practice.                      |

---

## Detailed Explanations

### 1. Bubble Sort

**Condition:** None (operates on unsorted or partially sorted collections).

#### Algorithm

1. Start from the last element and iterate backward to establish the boundary of the unsorted sub-array.
2. Compare each adjacent pair of elements from index 0 up to the current boundary.
3. If the left element is greater than the right element, swap them.
4. Continue adjacent comparisons until the boundary is reached; the largest unsorted element settles into its correct sorted position.
5. Repeat for the remaining unsorted portion.
6. If no swaps occur in a complete pass, terminate early as the array is already sorted.

#### Pseudocode

```text
BUBBLE_SORT(A, N)
1. For i = N - 1 down to 0
       DID_SWAP = False
       For j = 0 to i - 1
           If A[j] > A[j + 1]
               TEMP = A[j]
               A[j] = A[j + 1]
               A[j + 1] = TEMP
               DID_SWAP = True
       If DID_SWAP == False
           Break
2. Return A
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(N)** (when the array is already sorted, detected via the swap flag).
    - **Average Case:** **O(N^2)**.
    - **Worst Case:** **O(N^2)** (when the array is reverse sorted).
- **Space Complexity:** **O(1)** auxiliary space (in-place sorting).

<details>
<summary><b>Python Implementation</b></summary>

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        if not did_swap:
            break
    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void bubbleSort(std::vector<int>& arr) {
    int n = static_cast<int>(arr.size());
    for (int i = n - 1; i >= 0; --i) {
        bool didSwap = false;
        for (int j = 0; j < i; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                didSwap = true;
            }
        }
        if (!didSwap) {
            break;
        }
    }
}
```

</details>

- **Standalone Executables:** [Python Implementation](bubble_sort.py) | [C++ Implementation](bubble_sort.cpp)

---

### 2. Selection Sort

**Condition:** None (operates on unsorted collections).

#### Algorithm

1. Divide the array conceptually into a sorted prefix and an unsorted suffix.
2. For each position from 0 to N - 2, assume the current element is the minimum.
3. Scan through all subsequent elements in the unsorted suffix to locate the actual minimum element's index.
4. If a smaller element was found, swap it with the element at the current position.
5. Move the boundary of the sorted prefix one step to the right.
6. Repeat until the entire array is sorted.

#### Pseudocode

```text
SELECTION_SORT(A, N)
1. For i = 0 to N - 2
       MIN_IDX = i
       For j = i + 1 to N - 1
           If A[j] < A[MIN_IDX]
               MIN_IDX = j
       If MIN_IDX != i
           TEMP = A[i]
           A[i] = A[MIN_IDX]
           A[MIN_IDX] = TEMP
2. Return A
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(N^2)**.
    - **Average Case:** **O(N^2)**.
    - **Worst Case:** **O(N^2)**.
- **Space Complexity:** **O(1)** auxiliary space (in-place sorting).

<details>
<summary><b>Python Implementation</b></summary>

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void selectionSort(std::vector<int>& arr) {
    int n = static_cast<int>(arr.size());
    for (int i = 0; i < n - 1; ++i) {
        int minIdx = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            std::swap(arr[i], arr[minIdx]);
        }
    }
}
```

</details>

- **Standalone Executables:** [Python Implementation](selection_sort.py) | [C++ Implementation](selection_sort.cpp)

---

### 3. Insertion Sort

**Condition:** None (operates on unsorted collections; adaptive for nearly sorted inputs).

#### Algorithm

1. Treat the first element (index 0) as an already sorted sub-array.
2. Starting from index 1, designate the current element as the `key` to be inserted.
3. Compare the `key` with elements in the sorted portion moving from right to left.
4. Shift every element that is greater than `key` one position to the right.
5. Place `key` in the vacant position once an element smaller than or equal to `key` (or the beginning of array) is reached.
6. Repeat for all remaining elements until the entire collection is sorted.

#### Pseudocode

```text
INSERTION_SORT(A, N)
1. For i = 1 to N - 1
       KEY = A[i]
       j = i - 1
       While j >= 0 and A[j] > KEY
           A[j + 1] = A[j]
           j = j - 1
       A[j + 1] = KEY
2. Return A
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(N)** (when the array is already sorted, outer loop runs with no shifts).
    - **Average Case:** **O(N^2)**.
    - **Worst Case:** **O(N^2)** (when the array is in reverse order).
- **Space Complexity:** **O(1)** auxiliary space (in-place sorting).

<details>
<summary><b>Python Implementation</b></summary>

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void insertionSort(std::vector<int>& arr) {
    int n = static_cast<int>(arr.size());
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}
```

</details>

- **Standalone Executables:** [Python Implementation](insertion_sort.py) | [C++ Implementation](insertion_sort.cpp)

---

### 4. Merge Sort

**Condition:** None (Divide and Conquer approach; requires auxiliary memory).

#### Algorithm

1. If the array contains 0 or 1 element, it is already sorted; return immediately.
2. Find the midpoint index and divide the array into left and right halves.
3. Recursively sort the left half.
4. Recursively sort the right half.
5. Merge the two sorted halves:
    - Compare elements from both halves sequentially and insert the smaller element into a temporary buffer.
    - Copy any remaining elements once one half is exhausted.
6. Transfer the merged elements from the temporary buffer back into the original array.

#### Pseudocode

```text
MERGE(A, LOW, MID, HIGH)
1. Initialize LEFT = LOW, RIGHT = MID + 1, TEMP = empty array
2. While LEFT <= MID and RIGHT <= HIGH
       If A[LEFT] <= A[RIGHT]
           Append A[LEFT] to TEMP
           LEFT = LEFT + 1
       Else
           Append A[RIGHT] to TEMP
           RIGHT = RIGHT + 1
3. While LEFT <= MID
       Append A[LEFT] to TEMP
       LEFT = LEFT + 1
4. While RIGHT <= HIGH
       Append A[RIGHT] to TEMP
       RIGHT = RIGHT + 1
5. For i = LOW to HIGH
       A[i] = TEMP[i - LOW]

MERGE_SORT(A, LOW, HIGH)
1. If LOW < HIGH
       MID = (LOW + HIGH) / 2
       MERGE_SORT(A, LOW, MID)
       MERGE_SORT(A, MID + 1, HIGH)
       MERGE(A, LOW, MID, HIGH)
2. Return A
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(N log N)**.
    - **Average Case:** **O(N log N)**.
    - **Worst Case:** **O(N log N)**.
- **Space Complexity:** **O(N)** auxiliary space for temporary merging buffers.

<details>
<summary><b>Python Implementation</b></summary>

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
void merge(std::vector<int>& arr, int low, int mid, int high) {
    std::vector<int> temp;
    int left = low;
    int right = mid + 1;

    while (left <= mid && right <= high) {
        if (arr[left] <= arr[right]) {
            temp.push_back(arr[left++]);
        } else {
            temp.push_back(arr[right++]);
        }
    }

    while (left <= mid) {
        temp.push_back(arr[left++]);
    }

    while (right <= high) {
        temp.push_back(arr[right++]);
    }

    for (int i = low; i <= high; ++i) {
        arr[i] = temp[i - low];
    }
}

void mergeSortHelper(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int mid = low + (high - low) / 2;
        mergeSortHelper(arr, low, mid);
        mergeSortHelper(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

void mergeSort(std::vector<int>& arr) {
    if (!arr.empty()) {
        mergeSortHelper(arr, 0, static_cast<int>(arr.size()) - 1);
    }
}
```

</details>

- **Standalone Executables:** [Python Implementation](merge_sort.py) | [C++ Implementation](merge_sort.cpp)

---

### 5. Quick Sort

**Condition:** None (Divide and Conquer approach; in-place partitioning).

#### Algorithm

1. If the current sub-array boundary is invalid (`low >= high`), return.
2. Select a pivot element (e.g., the last element `arr[high]`).
3. Partition the array around the pivot:
    - Initialize pointer `i` before `low`.
    - Iterate with pointer `j` from `low` up to `high - 1`.
    - If `arr[j]` is smaller than the pivot, increment `i` and swap `arr[i]` with `arr[j]`.
    - After the loop, swap `arr[i + 1]` with the pivot `arr[high]`.
4. The pivot is now placed at its final sorted position `pi = i + 1`.
5. Recursively sort the left sub-array (from `low` to `pi - 1`).
6. Recursively sort the right sub-array (from `pi + 1` to `high`).

#### Pseudocode

```text
PARTITION(A, LOW, HIGH)
1. PIVOT = A[HIGH]
2. i = LOW - 1
3. For j = LOW to HIGH - 1
       If A[j] < PIVOT
           i = i + 1
           Swap A[i] with A[j]
4. Swap A[i + 1] with A[HIGH]
5. Return i + 1

QUICK_SORT_HELPER(A, LOW, HIGH)
1. If LOW < HIGH
       PI = PARTITION(A, LOW, HIGH)
       QUICK_SORT_HELPER(A, LOW, PI - 1)
       QUICK_SORT_HELPER(A, PI + 1, HIGH)

QUICK_SORT(A, N)
1. QUICK_SORT_HELPER(A, 0, N - 1)
2. Return A
```

#### Complexity Analysis

- **Time Complexity:**
    - **Best Case:** **O(N log N)** (balanced partitions).
    - **Average Case:** **O(N log N)**.
    - **Worst Case:** **O(N^2)** (unbalanced partitions, e.g. when already sorted with bad pivot selection).
- **Space Complexity:** **O(log N)** auxiliary stack space on average (**O(N)** worst case).

<details>
<summary><b>Python Implementation</b></summary>

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr
```

</details>

<details>
<summary><b>C++ Implementation</b></summary>

```cpp
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            ++i;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSortHelper(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortHelper(arr, low, pi - 1);
        quickSortHelper(arr, pi + 1, high);
    }
}

void quickSort(std::vector<int>& arr) {
    if (!arr.empty()) {
        quickSortHelper(arr, 0, static_cast<int>(arr.size()) - 1);
    }
}
```

</details>

- **Standalone Executables:** [Python Implementation](quick_sort.py) | [C++ Implementation](quick_sort.cpp)
