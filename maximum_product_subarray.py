class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        maxP = localMax = localMin = A[0]
        for i in A[1:]:
            if i > 0:
                localMax, localMin = max(localMax * i, i), min(localMin * i, i)
            else:
                localMax, localMin = max(localMin * i, i), min(localMax * i, i)
            maxP = max(maxP, localMax)
        return maxP