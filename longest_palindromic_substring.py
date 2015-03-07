class Solution:
	# @return a string
	def longestPalindrome(self, s):
		if len(s) == 0:
			return s
		res = ''
		for i in range(len(s)):
			p = self._longestPalindrome(s, i, i)
			if len(p) > len(res):
				res = p
			p = self._longestPalindrome(s, i, i + 1)
			if len(p) > len(res):
				res = p
		return res

	def _longestPalindrome(self, s, start, end):
		while start >= 0 and end < len(s) and s[start] == s[end]:
			start -= 1
			end += 1
		return s[start + 1: end]