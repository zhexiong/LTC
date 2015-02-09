class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        results = []
        self.subsetsHelper(S, 0, [], results)
        return results
        
    def subsetsHelper(self, S, index, result, results):
        if index == len(S):
            results.append(result[:])
            return
        result.append(S[index])
        self.subsetsHelper(S, index + 1, result, results)
        result.pop()
        self.subsetsHelper(S, index + 1, result, results)