from typing import List


class Solution:
    def missingNumber(self, nums: List[int]):
        result = len(nums)

        for i in range(len(nums)):
            result += (i - nums[i])


        return result

