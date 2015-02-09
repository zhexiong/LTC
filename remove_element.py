class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        index = 0
        for i in A:
            if i != elem:
                A[index] = i
                index += 1
        return index