# LeetCode #1: Two Sum (Easy)

[Problem Link](https://leetcode.com/problems/two-sum/)

## Analysis

The problem requires us to find indices of two numbers in an array that add up to a given `target` value. We are guaranteed exactly one solution, and we cannot use the same element twice.

---

## Brute Force Approach

We can use two nested loops to check all possible pairs of numbers.

### Algorithm

```python
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

### Complexity

- **Time Complexity:** **O(n^2)** because we check all pairs.
- **Space Complexity:** **O(1)** auxiliary space.

---

## Optimized Approach (One-Pass Hash Map)

Instead of searching for the second number in **O(n)** time, we can store each number's index in a hash map as we iterate. For each number, we check if its complement (`target - num`) is already present in our hash map.

### Algorithm

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsMap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in numsMap:
                return [numsMap[complement], idx]
            numsMap[num] = idx
```

### Complexity

- **Time Complexity:** **O(n)** as we traverse the list containing $N$ elements exactly once. Map lookups take **O(1)** time on average.
- **Space Complexity:** **O(n)** since in the worst case we will store all $N$ elements in the hash map.
