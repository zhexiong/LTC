class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or ch != s[i]:
                    return prefix
            prefix += ch
        return prefix