"""
https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/description/
"""


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        if n == 1:
            return 1
        dp = [[1, 1] for _ in range(n)]
        # the longest array that is finished with this number in [0] = num1 or [1] = num2
        dp[0] = [1, 1]
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                # the numbers in num1 are non-dec - we should continue the line with num1 numbers
                dp[i][0] = max(dp[i - 1][0] + 1, dp[i][0])
            if nums2[i] >= nums2[i - 1]:
                # the numbers in num2 are non-dec - we should continue the line with num2 numbers
                dp[i][1] = max(dp[i - 1][1] + 1, dp[i][1])
            if nums1[i] >= nums2[i - 1]:
                # the numbers in num1 >= num2 - we should choose between continuation of num1
                # which wwe checked previously, or add this thing (depending on what brings us higher number)
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
            if nums2[i] >= nums1[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
        return max([max(x) for x in dp])