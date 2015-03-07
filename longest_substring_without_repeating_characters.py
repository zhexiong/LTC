class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
    	maxLen = 0
    	indexMap = {}
    	start = 0
    	for i in range(len(s)):
    		if s[i] in indexMap:
    			if indexMap[s[i]] >= start:
    				start = indexMap[s[i]] + 1
			# update index of s[i]
			indexMap[s[i]] = i
			maxLen = max(maxLen, i - start + 1)
		return maxLen