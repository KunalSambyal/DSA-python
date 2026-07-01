# arrays.py
"""
Core guide to Lists (Dynamic Arrays) in Python for CP and DSA.
Covers:
1. Python Built-in Lists (Creation, Slicing, and Core Methods)
2. Essential Array Algorithms (Min/Max, Search, and Reverse)
"""


# =====================================================================
# 1. Python Lists (Built-in Dynamic Arrays)
# =====================================================================
def demo_python_lists():
    print("=" * 60)
    print(" 1. PYTHON LIST CREATION & METHODS ")
    print("=" * 60)

    # Creation Methods
    list_lit = [1, 2, 3, 4, 5]
    list_rep = [0] * 5  # Initializing with repeated values: [0, 0, 0, 0, 0]
    list_range = list(range(1, 6))  # [1, 2, 3, 4, 5]
    list_comp = [x**2 for x in range(5)]  # List Comprehension: [0, 1, 4, 9, 16]

    print(f"Literal list: {list_lit}")
    print(f"Repeated values: {list_rep}")
    print(f"Range-created: {list_range}")
    print(f"List Comprehension: {list_comp}")

    # Slicing: list[start:stop:step]
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"\nSlicing [1:4]: {fruits[1:4]}")
    print(f"Slicing [::-1] (Reverse): {fruits[::-1]}")

    # Core List Methods
    lst = [10, 20, 30]
    lst.append(40)  # Push to end
    print(f"\nAfter append(40): {lst}")

    lst.pop()  # Pop from end
    print(f"After pop(): {lst}")

    lst.insert(1, 15)  # Insert 15 at index 1
    print(f"After insert(1, 15): {lst}")

    lst.remove(15)  # Remove first occurrence of 15
    print(f"After remove(15): {lst}")

    lst.reverse()  # In-place reversal
    print(f"After reverse(): {lst}")

    lst.sort()  # In-place ascending sort
    print(f"After sort(): {lst}")


# =====================================================================
# 2. Essential Array Algorithms
# =====================================================================
def find_minimum(arr):
    if not arr:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


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


def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def demo_array_algorithms():
    print("\n" + "=" * 60)
    print(" 2. ESSENTIAL ARRAY ALGORITHMS ")
    print("=" * 60)

    data = [42, 7, 19, 88, 3, 55]
    print(f"Original Data: {data}")

    # Min Value
    print(f"Minimum Value: {find_minimum(data)}")

    # Linear Search
    print(f"Linear Search (Find 88): Index {linear_search(data, 88)}")

    # Binary Search (requires sorting first)
    sorted_data = sorted(data)
    print(f"Sorted Data for Binary Search: {sorted_data}")
    print(f"Binary Search (Find 88): Index {binary_search(sorted_data, 88)}")

    # In-place Reversal
    reverse_array_in_place(data)
    print(f"Data after in-place reversal: {data}")


if __name__ == "__main__":
    demo_python_lists()
    demo_array_algorithms()
