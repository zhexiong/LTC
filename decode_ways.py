class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if self.valid(s) else 0
        w1 = 1
        w2 = 1 if self.valid(s[0]) else 0
        for i in range(1, len(s)):
            w3 = 0
            if self.valid(s[i:i+1]):
                w3 += w2
            if self.valid(s[i-1:i+1]):
                w3 += w1
            w1 = w2
            w2 = w3
        return w2
        
    def valid(self, s):
        return s[0] != '0' and int(s) <= 26 and int(s) >= 1

"""
Recursion, TLE
"""
class Solution2:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 1
        if len(s) == 1:
            return 1 if self.valid(s) else 0
        ways = 0
        if self.valid(s[-1:]):
            ways += self.numDecodings(s[:-1])
        if self.valid(s[-2:]):
            ways += self.numDecodings(s[:-2])
        return ways
        
    def valid(self, s):
        return s[0] != '0' and int(s) <= 26 and int(s) >= 1