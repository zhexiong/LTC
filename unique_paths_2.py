class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0:
            return 0
        paths = [[0 for x in range(len(obstacleGrid[0]))] for x in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and j > 0:
                        paths[i][j] = paths[i - 1] [j] + paths[i][j - 1]
                elif i > 0:
                    paths[i][j] = paths[i - 1] [j]
                elif j > 0:
                    paths[i][j] = paths[i][j - 1]
                else:
                    paths[i][j] = 1
        return paths[-1][-1]