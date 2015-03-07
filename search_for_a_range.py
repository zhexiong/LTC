class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        i = 0
        j = len(A) - 1
        while i <= j:
            mid = (i + j) / 2
            if target == A[mid]:
                low = high = mid
                while low >= 0 and target == A[low]:
                    low -= 1
                while high < len(A) and target == A[high]:
                    high += 1
                return [low + 1, high - 1]
            elif target > A[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return [-1, -1]