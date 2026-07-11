# linear_search.py
"""
Linear Search implementation in Python.
Covers:
1. Linear Search Algorithm
"""

# =====================================================================
# 1. Linear Search
# =====================================================================
def linear_search(arr, target):
    """
    Performs Linear Search on a list to find the target element.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def demo_linear_search():
    print("=" * 60)
    print(" 1. LINEAR SEARCH ")
    print("=" * 60)

    data = [2, 12, 5, 8, -16, 23, -38, 56, 72, 91]
    target = 23
    print(f"Array: {data}")
    print(f"Target: {target}")
    result = linear_search(data, target)
    print(f"Target found at index: {result}")

    target_missing = 50
    print(f"\nTarget: {target_missing}")
    result_missing = linear_search(data, target_missing)
    print(f"Target found at index: {result_missing}")


if __name__ == "__main__":
    demo_linear_search()