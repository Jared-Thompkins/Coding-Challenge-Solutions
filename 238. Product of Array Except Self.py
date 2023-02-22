from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        acc = 1
        for n in nums:
            result.append(acc)
            acc *= n

        acc = 1
        for i in reversed(range(len(nums))):
            result[i] *= acc
            acc *= nums[i]

        return result
