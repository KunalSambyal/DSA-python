# valid_palindrome.py
"""
LeetCode #125: Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(1)
"""

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

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))