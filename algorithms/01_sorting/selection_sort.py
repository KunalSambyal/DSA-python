# selection_sort.py
"""
Selection Sort implementation in Python.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
print("Array before sort:", arr)
print("Array after sort:", selection_sort(arr))