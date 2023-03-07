class Solution:
    def moveZeroes(self, nums):
        l = 0

        for r in range(len(nums)):
            if nums[r]:             #Translates to if not 0.
                nums[l], nums[r] = nums[r], nums[l]
                l += 1