class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        dp_table = [[0 for x in range(len(grid[0]))] for x in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    dp_table[i][j] = grid[i][j] + min(dp_table[i - 1][j], dp_table[i][j - 1])
                elif i > 0:
                    dp_table[i][j] = grid[i][j] + dp_table[i - 1][j]
                elif j > 0:
                    dp_table[i][j] = grid[i][j] + dp_table[i][j - 1]
                else:
                    dp_table[i][j] = grid[i][j]
        return dp_table[-1][-1]