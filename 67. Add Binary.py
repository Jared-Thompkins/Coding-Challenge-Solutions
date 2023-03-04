class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a = a[::-1]     #reverse str to make it closer to hand mathematics.
        b = b[::-1]

        for i in range(max(len(a) , len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0      #In bounds check. Then converts character to int.
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res        #The program goes digit by digit.
            carry = total // 2

        if carry:
            res = "1" + res
        return res