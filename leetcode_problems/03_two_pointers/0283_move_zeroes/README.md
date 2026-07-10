# LeetCode #283: Move Zeroes (Easy)

[Problem Link](https://leetcode.com/problems/move-zeroes/)

## Analysis

The problem requires us to move all zeroes in an integer array `nums` to the end, while maintaining the relative order of the non-zero elements. The operations must be performed in-place without making a copy of the array.

---

## Brute Force Approach

Create a temporary array to store all non-zero elements. Then, fill the remaining elements in the temporary array with zeroes, and copy all elements back to the original array.

### Algorithm

```python
def moveZeroes(nums: list[int]) -> None:
    temp = []
    # Collect all non-zero elements
    for num in nums:
        if num != 0:
            temp.append(num)

    # Pad the remaining spaces with zeroes
    while len(temp) < len(nums):
        temp.append(0)

    # Copy back to the original array
    for i in range(len(nums)):
        nums[i] = temp[i]
```

### Complexity

- **Time Complexity:** **O(N)** where **N** is the size of the array, as we iterate through the list to filter, pad, and copy.
- **Space Complexity:** **O(N)** auxiliary space to store the temporary array.

---

## Optimized Approach (Two Pointers - Read/Write)

We can solve this problem in a single pass using a slow-pointer (`left`) and a fast-pointer (`right`).

### Algorithm

1. Initialize `left` (write pointer) to 0.
2. Iterate `right` (read pointer) through the array from `0` to `len(nums) - 1`.
3. If the element at `right` is non-zero:
    - Swap `nums[left]` and `nums[right]`.
    - Increment `left` by 1.
4. Swapping ensures that non-zero elements are shifted to the left, while zero elements naturally bubble to the right in-place.

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
```

### Complexity

- **Time Complexity:** **O(N)** where **N** is the size of the array, as we iterate through the list exactly once.
- **Space Complexity:** **O(1)** auxiliary space since we perform all swaps in-place.
