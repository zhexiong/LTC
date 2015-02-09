class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num) == 0:
            return 0
        num.sort()
        results = []
        visited = {x:False for x in range(len(num))}
        self.permuteUniqueHelper(num, len(num), visited, [], results)
        return results
        
    def permuteUniqueHelper(self, num, count, visited, result, results):
        if len(result) == count:
            results.append(result[:])
            return
        while i < len(num):
            if not visited[i] and (i == 0 or num[i] != num[i - 1] or not visited[i - 1]):
                result.append(num[i])
                visited[i] = True
                self.permuteUniqueHelper(num, count, visited, result, results)
                result.pop()
                visited[i] = False
            