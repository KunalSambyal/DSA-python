# two_sum.py
"""
LeetCode #1: Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(N)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsMap = {} 
        for idx, num in enumerate(nums):
            complement = target - num
            if(complement in numsMap):
                return [numsMap[complement], idx]
                
            numsMap[num] = idx


arr = [2, 7, 11, 15]
target = 9

sol = Solution()

print(sol.twoSum(arr, target))