class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        dp = [False for x in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in dict:
                dp[i] = True
            for j in range(i):
                if dp[j] and s[j+1:i+1] in dict:
                    dp[i] = True
        if not dp[len(s) - 1]:
            return []
        results = []
        self.dfs(s, 0, [], results, dict)
        return results
    
    def dfs(self, s, index, result, results, dict):
        if index == len(s):
            results.append(' '.join(result[:]))
            return
        for i in range(index+1, len(s)+1):
            if s[index:i] in dict:
                result.append(s[index:i])
                self.dfs(s, i, result, results, dict)
                result.pop()