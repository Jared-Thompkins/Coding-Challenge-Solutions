from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        output = 0
        odd = 0

        if len(c) == 1:
            return c[s[0]]

        for i in c.values():
            if i > 1:
                if i % 2 == 0:
                    output += i
                else:
                    output += i - 1
                    odd += 1
            else:
                odd += 1

        if odd > 0:
            output += 1
        return output

