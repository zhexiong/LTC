class Solution:
    # @return a boolean
    def isMatch(self, s, p):
    	if (len(p) == 0):
    		return len(s) == 0
    	if len(s) > 0:
			if len(p) > 1 and p[1] == '*':
				return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
			else:
				return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
    	elif len(p) > 1 and p[1] == '*':
    		return self.isMatch(s, p[2:])
    	else:
    		return False