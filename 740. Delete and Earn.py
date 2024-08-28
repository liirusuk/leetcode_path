"""
https://leetcode.com/problems/delete-and-earn/description/
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {} # keeping maximum we can get by taking the number
        for entry in nums:
            d.setdefault(entry, 0)
            d[entry] += entry
        sorted_keys = sorted(d.keys())
        # now imagine if x is maximum number we take, how much can we earn?
        dp = [0]*(sorted_keys[-1]+1)
        dp[0] = d.get(0,0)
        dp[1] = d.get(1,0)
        for i in range(2,sorted_keys[-1]+1):
            # if we take dp[i], we will have to say bye to i-1
            # then we should get a maximum between taking i-2 or i-3
            # (because it will only be one of them)
            dp[i] = d.get(i, 0) + max(dp[i-2], dp[i-3])
        return max(dp)