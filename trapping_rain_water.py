class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        lmax = []
        maxNum = 0
        for n in A:
            lmax.append(maxNum)
            maxNum = max(maxNum, n)
        area = 0
        maxNum = 0
        for i in reversed(range(len(A))):
            diff = min(lmax[i], maxNum) - A[i]
            if diff > 0:
                area += diff
            maxNum = max(maxNum, A[i])
        return area