class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        results = []
        self.helper(candidates, 0, target, [], results)
        return results
        
    def helper(self, candidates, index, target, result, results):
        if target == 0:
            results.append(result[:])
            return
        if index == len(candidates) or target < 0:
            return
        result.append(candidates[index])
        self.helper(candidates, index + 1, target - candidates[index], result, results)
        num = result.pop()
        while index < len(candidates) and candidates[index] == num:
            index += 1
        self.helper(candidates, index, target, result, results)