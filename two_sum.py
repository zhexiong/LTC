class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
    	numMap = {}
    	for index in range(len(num)):
    		temp = target - num[index]
    		if temp in numMap:
    			return (numMap[temp] + 1, index + 1)
    		elif num[index] not in numMap:
    			numMap[num[index]] = index