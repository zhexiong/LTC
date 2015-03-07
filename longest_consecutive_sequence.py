class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        numMap = {}
        for i in num:
            if i not in numMap:
                numMap[i] = True
        maxLen = 0
        for i in num:
            count = 0
            low = i
            while low in numMap:
                count += 1
                numMap.pop(low)
                low -= 1
            high = i + 1
            while high in numMap:
                count += 1
                numMap.pop(high)
                high += 1
            maxLen = max(maxLen, count)
        return maxLen