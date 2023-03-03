class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a = a[::-1]     #reverse str
        b = b[::-1]

        for i in range(max(len(a) , len(b))):
            digitA = a[i] if i < len(a) else 0
            digitB = b[i] if i < len(b) else 0