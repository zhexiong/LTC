class Solution:
    # @return an integer
    def reverse(self, x):
        flag = -1 if x < 0 else 1
        reversed_x = 0
        x = abs(x)
        while x:
            reversed_x *= 10
            reversed_x += x % 10
            x = x / 10
        reversed_x *= flag
        return reversed_x if reversed_x < 2 ** 31 - 1 and reversed_x > - 2 ** 31 else 0