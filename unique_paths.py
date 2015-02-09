class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        paths = [[1 for x in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                elif i > 0:
                    paths[i][j] = paths[i - 1][j]
                elif j > 0:
                    paths[i][j] = paths[i][j - 1]
                else:
                    paths[i][j] = 1
        return paths[-1][-1]