# valid_parentheses.py
"""
LeetCode #20: Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(N)
"""


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


sol = Solution()
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
s5 = "([)]"

print(sol.isValid(s1))
print(sol.isValid(s2))
print(sol.isValid(s3))
print(sol.isValid(s4))
print(sol.isValid(s5))