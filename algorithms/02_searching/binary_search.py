# binary_search.py
"""
Binary Search implementations in Python.
Covers:
1. Iterative Binary Search
2. Recursive Binary Search
"""

# =====================================================================
# 1. Iterative Binary Search
# =====================================================================
def binary_search_iterative(arr, target):
    """
    Performs Binary Search iteratively.
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
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


def demo_iterative_search():
    print("=" * 60)
    print(" 1. ITERATIVE BINARY SEARCH ")
    print("=" * 60)

    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    print(f"Array: {data}")
    print(f"Target: {target}")
    result = binary_search_iterative(data, target)
    print(f"Target found at index: {result}")

    target_missing = 50
    print(f"\nTarget: {target_missing}")
    result_missing = binary_search_iterative(data, target_missing)
    print(f"Target found at index: {result_missing}")


# =====================================================================
# 2. Recursive Binary Search
# =====================================================================
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
    """
    Performs Binary Search recursively.
    Time Complexity: O(log N)
    Space Complexity: O(log N) auxiliary space for call stack
    """
    return binary_search_recursive_helper(arr, target, 0, len(arr) - 1)


def demo_recursive_search():
    print("\n" + "=" * 60)
    print(" 2. RECURSIVE BINARY SEARCH ")
    print("=" * 60)

    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    print(f"Array: {data}")
    print(f"Target: {target}")
    result = binary_search_recursive(data, target)
    print(f"Target found at index: {result}")

    target_missing = 50
    print(f"\nTarget: {target_missing}")
    result_missing = binary_search_recursive(data, target_missing)
    print(f"Target found at index: {result_missing}")


if __name__ == "__main__":
    demo_iterative_search()
    demo_recursive_search()
