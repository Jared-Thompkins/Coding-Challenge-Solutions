class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        carry = 1
        idx = 0

        while carry:
            if idx < len(digits):           #In bounds check.
                if digits[idx] == 9:
                    digits[idx] = 0
                else:
                    digits[idx] += 1        #Add (1) to that digit in the list.
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            idx += 1                #Move on to the next item in the list.
        return digits[::-1]