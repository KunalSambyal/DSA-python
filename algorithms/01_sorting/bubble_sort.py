# bubble_sort.py
"""
Bubble Sort implementation in Python.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        did_swap = False

        for j in range(i):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                did_swap = True

        if not did_swap:
            break

    return arr

arr = [64, -34, 25, 12, 22, 11, 90]
print("Array before sort:", arr)
print("Array after sort:", bubble_sort(arr))

