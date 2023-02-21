from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = {}

        for i in range(len(nums)):
            if t.get(nums[i]):
                return True
            else:
                t[nums[i]] = True
        return False

s = Solution()

print(s.containsDuplicate(nums = [1,2,3,1]))
print(s.containsDuplicate(nums = [1,2,3,4]))
print(s.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
