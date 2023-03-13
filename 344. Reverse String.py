class Solution:
    def reverseString(self, s):
        l, r = 0 , len(s) - 1       #-1 b/c we will use as index in the future.

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1