# insertion_sort.py
"""
Insertion Sort implementation in Python.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

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

arr = [64, 25, 12, 22, 11]
print("Array before sort:", arr)
print("Array after sort:", insertion_sort(arr))
