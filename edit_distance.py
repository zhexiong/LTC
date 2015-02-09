class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dist = [[0 for x in range(len(word2) + 1)] for x in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i > 0 and j > 0:
                    diff = 0 if word1[i - 1] == word2[j - 1] else 1
                    dist[i][j] = min(dist[i - 1][j] + 1, dist[i][j - 1] + 1, dist[i - 1][j - 1] + diff)
                elif i > 0:
                    dist[i][j] = dist[i - 1][j] + 1
                elif j > 0:
                    dist[i][j] = dist[i][j - 1] + 1
        return dist[-1][-1]