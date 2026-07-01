# valid_anagram.py
"""
LeetCode #242: Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(1) (fixed lowercase English character set)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if (char not in count or count[char] == 0):
                return False
            count[char] -= 1
        
        return True
    
sol = Solution()
s = "anagram"
t = "nagara"
print(sol.isAnagram(s, t))