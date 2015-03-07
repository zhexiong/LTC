class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) < 2:
            return 0
        steps = 1
        start = 0
        end = A[0]
        while end < len(A) - 1:
            reach = end
            for i in range(start, end + 1):
                reach = max(reach, i + A[i])
            start = end + 1
            end = reach
            steps += 1
        return steps