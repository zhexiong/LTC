class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0
        indexStack = []
        maxLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                indexStack.append(i)
            else:
                if len(indexStack) > 0 and s[indexStack[-1]] == '(':
                    indexStack.pop()
                    last = -1
                    if len(indexStack) > 0:
                        last = indexStack[-1]
                    length = i - last
                    if maxLen < length:
                        maxLen = length
                else:
                    indexStack.append(i)
        return maxLen