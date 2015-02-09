class Solution:
    # @return an integer
    def numTrees(self, n):
        if n < 2:
            return 1
        count = [0 for x in range(n+1)]
        count[0] = count[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                count[i] += count[j] * count[i - j - 1]
        return count[-1]