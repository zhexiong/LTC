class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == self.reverse(x):
            return True
        return False
        
    def reverse(self, x):
    	reversed_x = 0
        while x > 0:
        	reversed_x *= 10
        	reversed_x += x % 10
        	x = x / 10
        return reversed_x