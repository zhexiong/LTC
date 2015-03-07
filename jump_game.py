class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
    	reach = 0
    	for i in range(len(A)):
    		reach = max(reach, i + A[i])
    		if reach >= len(A) - 1:
    			return True
			if reach == i:
				return False
		return True