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

- **File:** [bubble_sort.py](bubble_sort.py)
- **Concept:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This pass is repeated until the list is sorted.
- **Optimization:** Uses a boolean flag `did_swap`. If no swaps occur in a full pass, the array is already sorted, yielding a best-case time complexity of **O(N)**.

### 2. Selection Sort

- **File:** [selection_sort.py](selection_sort.py)
- **Concept:** Divides the input list into a sorted sublist and an unsorted sublist. It repeatedly finds the minimum element from the unsorted sublist and moves it to the end of the sorted sublist.
- **Key Feature:** Performs a maximum of **O(N)** swaps, making it useful when write operations are significantly more expensive than read operations.

### 3. Insertion Sort

- **File:** [insertion_sort.py](insertion_sort.py)
- **Concept:** Builds the final sorted array one element at a time by inserting each new element into its correct relative position within the already sorted part of the array.
- **Key Feature:** Highly efficient for small datasets and adaptive (runs in **O(N)** time if the array is already sorted).

### 4. Merge Sort

- **File:** [merge_sort.py](merge_sort.py)
- **Concept:** A Divide and Conquer algorithm. It divides the array into two halves, recursively sorts them, and then merges the two sorted halves back together.
- **Key Feature:** Offers guaranteed **O(N log N)** performance but requires **O(N)** auxiliary space for the merge step.

### 5. Quick Sort

- **File:** [quick_sort.py](quick_sort.py)
- **Concept:** A Divide and Conquer algorithm. It selects a "pivot" element and partitions the array such that elements smaller than the pivot are on its left and larger elements are on its right. It then recursively sorts the sub-arrays.
- **Key Feature:** Typically faster in practice than Merge Sort due to smaller constant factors and in-place partitioning, though its worst-case complexity is **O(N^2)**.
