# LeetCode #242: Valid Anagram (Easy)

[Problem Link](https://leetcode.com/problems/valid-anagram/)

## Analysis

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. Thus, the two strings must have identical lengths and the exact same count of each character.

---

## Brute Force Approach (Sorting)

If two strings are anagrams, sorting their characters alphabetically will produce identical sorted strings.

### Algorithm

```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

### Complexity

- **Time Complexity:** **O(n log n)** due to sorting, where $n$ is the length of the string.
- **Space Complexity:** **O(n)** for sorting allocations.

---

## Optimized Approach (Frequency Map / Hash Table)

We count the occurrences of each character in string `s` using a hash map (or fixed-size array). Then, we iterate through string `t` and decrement the character counts. If we encounter a character not in our map or its count drops below zero, the strings are not anagrams.

### Algorithm

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True
```

### Complexity

- **Time Complexity:** **O(n)** because we iterate through the strings of length $n$ a constant number of times.
- **Space Complexity:** **O(1)** auxiliary space if the character set is fixed (e.g., 26 lowercase English letters), or **O(n)** in the worst case if storing arbitrary Unicode characters.
