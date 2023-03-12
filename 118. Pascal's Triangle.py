class Solution:
    def generate(self, numRows: int):
        res = [[1]]

        for i in range(numRows - 1):   #excluding first row made above.
            temp = [0] + res[-1] + [0]      #joining arrays of 0 with array above.
            single_row = []
            for j in range(len(res[-1]) + 1):   #we are growing output for each numRow.
                single_row.append(temp[j] + temp[j+1])
            res.append(single_row)
        return res