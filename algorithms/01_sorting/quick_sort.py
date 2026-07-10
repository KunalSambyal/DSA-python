# quick_sort.py
"""
Quick Sort implementation in Python.
Time Complexity: O(N log N) average, O(N^2) worst case
Space Complexity: O(log N) auxiliary space for call stack
"""

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

arr = [64, 25, 12, 22, 11]
print("Array before sort:", arr)
print("Array after sort:", quick_sort(arr))
