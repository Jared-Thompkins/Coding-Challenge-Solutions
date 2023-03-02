# def isBadVersion(version: int):

class Solution:
    def firstBadVersion(self, n:int):
        l , r = 1 , n

        while (l < r):
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return r