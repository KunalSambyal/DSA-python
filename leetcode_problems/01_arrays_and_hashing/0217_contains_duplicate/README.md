# LeetCode #217: Contains Duplicate (Easy)

[Problem Link](https://leetcode.com/problems/contains-duplicate/)

## Analysis

The problem asks us to determine if any element in an array appears at least twice. If all elements are distinct, we should return `False`; otherwise, return `True`.

---

## Brute Force Approach

Compare every element with every other element in the array using nested loops.

### Algorithm

```python
def containsDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```

### Complexity

- **Time Complexity:** **O(n^2)** due to the nested comparison loops.
- **Space Complexity:** **O(1)** auxiliary space.

---

## Sorting Approach

Sort the array first. If there are duplicates, they will end up adjacent to each other. We then traverse the sorted array and compare each element to its neighbor.

### Algorithm

```python
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
```

### Complexity

- **Time Complexity:** **O(n log n)** to sort the array.
- **Space Complexity:** **O(1)** or **O(n)** depending on the sorting implementation.

---

## Optimized Approach (Using Hash Set)

We can trade space for time by using a Hash Set to track the numbers we have already seen as we iterate through the list.

### Algorithm

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

### Complexity

- **Time Complexity:** **O(n)** because set insertions and lookups operate in **O(1)** average time.
- **Space Complexity:** **O(n)** since in the worst case we store all distinct elements in the set.
