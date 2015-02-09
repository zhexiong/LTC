class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if int(s) <= 26 and int(s) >= 1 else 0
        # decode = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        w1 = 1 if self.valid(s[0]) else 0
        w2 = 1 if s[0] != '0' and self.valid(s[:2]) else 0
        w2 += w1 if self.valid(s[1]) else 0
        for i in range(2, len(s)):
            w3 = 0
            if self.valid(s[i:i+1]):
                w3 += w2
            if s[i-1] != '0' and self.valid(s[i-1:i+1]):
                w3 += w1
            w1 = w2
            w2 = w3
        return w2
        
    def valid(self, s):
        return int(s) <= 26 and int(s) >= 1