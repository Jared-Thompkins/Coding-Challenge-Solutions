class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

