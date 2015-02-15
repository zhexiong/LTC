class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
    	matrix = [[0 for x in range(n)] for x in range(n)]
    	start = 0
    	end = n - 1
    	num = 0
    	while start < end:
    		for i in range(start, end):
    			num += 1
    			matrix[start][i] = num
			for i in range(start, end):
				num += 1
				matrix[i][end] = num
			for i in range(end, start, -1):
				num += 1
				matrix[end][i] = num
			for i in range(end, start, -1):
				num += 1
				matrix[i][start] = num
			start += 1
			end -= 1
		if start == end:
			matrix[start][end] = num + 1
		return matrix