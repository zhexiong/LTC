class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[] for x in range(numRows)]
        res[0] = [1]
        for i in range(1, numRows):
            res[i].append(1)
            for j in range(len(res[i - 1]) - 1):
                res[i].append(res[i - 1][j] + res[i - 1][j + 1])
            res[i].append(1)
        return res