"""
https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/
"""


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count0 = [0, 0]
        sums = [0, 0]
        # first we need to know the sums and how many numbers
        # we need to replace in both arrays
        for i in nums1:
            sums[0] += i
            if i == 0:
                count0[0] += 1
        for i in nums2:
            sums[1] += i
            if i == 0:
                count0[1] += 1

        if count0[0] == 0:
            if sums[0] < sums[1]:
                # eliminate the example 2
                return -1

            if count0[1] == 0:
                if sums[0] == sums[1]:
                    # all good
                    return sums[0]
                else:
                    # we can't do anything
                    return -1
            if count0[1] > (sums[0] - sums[1]):
                # we can't do anything
                return -1
        if count0[1] == 0:
            if sums[1] < sums[0]:
                # eliminate the example 2
                return -1

            if count0[0] > (sums[1] - sums[0]):
                # we can't do anything
                return -1
        # otherwise - replace everything by 1s an check where sum is max -
        # then we'll match the other
        return max(sums[0] + count0[0], sums[1] + count0[1])
