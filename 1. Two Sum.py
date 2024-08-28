"""
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        things are pretty easy: if we have a number target-x, then let's give the answer,
        otherwise we add "number" into a dict, remembering it's position.
        """
        dict_numbers = {}
        for i, n in enumerate(nums):
            pair = dict_numbers.get(target-n)
            if pair is not None:
                return [pair, i]
            else:
                dict_numbers[n] = i
        return []