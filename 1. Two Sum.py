from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        d = {}

        for index, value in enumerate(nums):
            r = target - value
            if r in d:
                return [d[r], index]
            d[value] = index

