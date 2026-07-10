# group_anagrams.py
"""
LeetCode #49: Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams/

Complexity:
- Time Complexity: O(N * K log K) where N is the number of strings, and K is the max length of a string.
- Space Complexity: O(N * K)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map = defaultdict(list)
        
        for word in strs:
            # Sort the characters of the word to form the key
            sorted_key = "".join(sorted(word))
            anagrams_map[sorted_key].append(word)
            
        return list(anagrams_map.values())

sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Grouped Anagrams:", sol.groupAnagrams(strs))