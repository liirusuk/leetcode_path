"""
https://leetcode.com/problems/maximum-subarray/description/
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        max_sum = nums[0]
        for n in nums[1:]:
            dp.append(max(n, n + dp[-1]))
            max_sum = max(dp[-1], max_sum)
        return max_sum
