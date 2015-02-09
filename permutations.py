class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        results = []
        visited = [False for x in range(len(num))]
        self.permuteHelper(num, visited, [], results)
        return results
    
    def permuteHelper(self, num, visited, result, results):
        if len(result) == len(num):
            results.append(result[:])
            return
        for i in range(len(num)):
            if not visited[i]:
                result.append(num[i])
                visited[i] = True
                self.permuteHelper(num, visited, result, results)
                result.pop()
                visited[i] = False