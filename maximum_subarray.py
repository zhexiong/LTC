class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return 0
        maxSum = preMax = A[0]
        for i in range(1, len(A)):
            preMax = max(preMax + A[i], A[i])
            maxSum = max(maxSum, preMax)
        return maxSum