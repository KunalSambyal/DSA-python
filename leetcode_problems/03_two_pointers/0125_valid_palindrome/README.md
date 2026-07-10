# LeetCode #125: Valid Palindrome (Easy)

[Problem Link](https://leetcode.com/problems/valid-palindrome/)

## Analysis

The problem requires us to check if a string is a palindrome. A palindrome is a phrase that reads the same backward as forward, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.

---

## Brute Force Approach

Filter out all non-alphanumeric characters, convert them to lowercase, reverse the resulting list, and compare it to the original filtered list.

### Algorithm

```python
def isPalindrome(s: str) -> bool:
    filtered = [char.lower() for char in s if char.isalnum()]
    return filtered == filtered[::-1]
```

### Complexity

- **Time Complexity:** **O(N)** where **N** is the length of the string, since we traverse the string to filter, reverse, and compare.
- **Space Complexity:** **O(N)** because we create a new filtered list of characters.

---

## Optimized Approach (Two Pointers)

Instead of creating a new filtered string, which would consume **O(N)** extra space, we can use two pointers (left and right) starting at the beginning and the end of the string.

### Algorithm

1. Initialize `left` pointer to 0 and `right` pointer to `len(s) - 1`.
2. While `left < right`:
    - Increment `left` if the character at `left` is not alphanumeric.
    - Decrement `right` if the character at `right` is not alphanumeric.
    - Compare the lowercase characters at `left` and `right`. If they are not equal, return `False`.
    - Otherwise, increment `left` and decrement `right` to check the next pair.
3. If all valid characters match, return `True`.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

### Complexity

- **Time Complexity:** **O(N)** where **N** is the length of the string `s`, since we traverse the string at most once.
- **Space Complexity:** **O(1)** as we perform the checks in-place using two index pointers.
