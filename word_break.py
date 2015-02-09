class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return False
        canBreak = [False for x in range(len(s))]
        for i in range(0, len(s)):
            if s[:i + 1] in dict:
                canBreak[i] = True
            else:
                for j in range(i):
                    if canBreak[j] and s[j+1:i+1] in dict:
                        canBreak[i] = True
                        break
        return canBreak[len(s) - 1]