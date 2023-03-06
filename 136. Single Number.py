class Solution:
    def singleNumber(self, nums):
        res = 0

        for n in nums:
            res = n ^ res   #duplicate n's cancel each other out. We are left with res in binary.
        return res