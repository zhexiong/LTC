class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
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
        current = result.pop()
        while index < len(S) and S[index] == current:
            index += 1
        self.subsetsHelper(S, index, result, results)
        