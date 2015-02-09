class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        num = [[0 for x in range(len(T)+1)] for x in range(len(S)+1)]
        for i in range(0, len(S)+1):
            num[i][0] = 1
        for i in range(1, len(T)+1):
            num[0][i] = 0
        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                if i >= j:
                    if S[i-1] == T[j-1]:
                        num[i][j] = num[i-1][j-1] + num[i-1][j]
                    else:
                        num[i][j] = num[i-1][j]
        return num[-1][-1]