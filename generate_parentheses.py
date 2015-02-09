class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        results = []
        self.generateParenthesisHelper(n, n, '', results)
        return results
        
    def generateParenthesisHelper(self, left, right, result, results):
        if left == 0 and right == 0:
            results.append(result[:])
            return
        if right > left:
            self.generateParenthesisHelper(left, right - 1, result + ')', results)
        if left > 0:
            self.generateParenthesisHelper(left - 1, right, result + '(', results)