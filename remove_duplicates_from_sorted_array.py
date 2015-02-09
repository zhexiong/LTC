class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        last = A[0]
        index = 1
        for i in A[1:]:
            if i != last:
                A[index] = i
                last = i
                index += 1
        return index