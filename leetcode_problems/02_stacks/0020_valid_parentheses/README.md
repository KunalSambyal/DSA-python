# LeetCode #20: Valid Parentheses (Easy)

[Problem Link](https://leetcode.com/problems/valid-parentheses/)

## Analysis

The problem asks us to determine if an input string containing only parenthesis characters (`(`, `)`, `{`, `}`, `[`, `]`) is valid. A string is valid if open brackets are closed by the same type of brackets, closed in the correct order, and every close bracket has a matching open bracket.

---

## Brute Force Approach

Repeatedly search for adjacent matching pairs of brackets (`()`, `[]`, or `{}`) in the string and replace them with empty strings. Keep doing this until no matching pairs can be found. If the final string is empty, the input string is valid; otherwise, it is invalid.

### Algorithm

```python
def isValid(s: str) -> bool:
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return len(s) == 0
```

### Complexity

- **Time Complexity:** **O(N^2)** because in the worst case, we perform string search and replacement operations of size **O(N)** up to **N/2** times.
- **Space Complexity:** **O(N)** due to string creation during replacements.

---

## Optimized Approach (Using a Stack)

A stack is the perfect data structure for this problem because the last bracket opened must be the first one closed (LIFO - Last In First Out).

### Algorithm

1. Initialize an empty stack.
2. Define a hash map to map each closing bracket to its corresponding opening bracket.
3. Iterate through each character in the string:
    - If the character is a closing bracket, pop the top element from the stack (or use a dummy character like `#` if the stack is empty). If the popped element does not match the mapped opening bracket, return `False`.
    - If the character is an opening bracket, push it onto the stack.
4. After the loop, return `True` if the stack is empty (meaning all brackets were matched), otherwise return `False`.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not(stack)
```

### Complexity

- **Time Complexity:** **O(N)** because we traverse the string of length **N** exactly once, and stack operations (`push`, `pop`) take **O(1)** time.
- **Space Complexity:** **O(N)** since in the worst case (e.g., `((((((`), we push all characters onto the stack.
