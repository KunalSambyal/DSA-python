# contains_duplicate.py
"""
LeetCode #217: Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(N)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if(num in seen):
                return True
            seen.add(num)
        return False

sol = Solution()
nums = [1, 2, 3, 4]
print(sol.containsDuplicate(nums))