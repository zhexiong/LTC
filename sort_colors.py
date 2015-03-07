class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i = start = 0
        end = len(A) - 1
        while i <= end:
            if A[i] == 0:
                # num berfor i should always be in right order.
                A[start], A[i] = A[i], A[start]
                start += 1
                # make sure i never be smaller then start.
                i += 1
            elif A[i] == 2:
                A[end], A[i] = A[i], A[end]
                end -= 1
            else:
                i += 1

class Solution2:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i = start = 0
        end = len(A) - 1
        while i < len(A):
            if A[i] == 0 and start < i:
                A[start], A[i] = A[i], A[start]
                start += 1
            elif A[i] == 2 and end > i:
                A[end], A[i] = A[i], A[end]
                end -= 1
            # A[i] is 1, or i < start, or i > end, 
            # which means the number on the pos is right.
            else:
                i += 1

class Solution3:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        zero_pos = one_pos = two_pos = 0
        for i in A:
            if i == 0:
                A[two_pos] = 2
                A[one_pos] = 1
                A[zero_pos] = 0
                two_pos += 1
                one_pos += 1
                zero_pos += 1
            elif i == 1:
                A[two_pos] = 2
                A[one_pos] = 1
                two_pos += 1
                one_pos += 1
            elif i == 2:
                A[two_pos] = 2
                two_pos += 1