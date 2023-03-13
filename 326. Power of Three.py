class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        output = 1       #the first output for the powers of 3 (3^0 = 1).
        power = 0    #the powers.

        while output <= n:
            if output == n:     #it will do so if its 3 ** any real int.
                return True
            power += 1
            output = 3 ** power
        return False