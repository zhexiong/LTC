class Solution:
    # @return an integer
    def atoi(self, str):
        if len(str) == 0:
            return 0
        str = str.strip()
        sign = 1
        i = 0
        if str[0] == '-':
            sign = -1
            i += 1
        elif str[0] == '+':
            i += 1
        length = len(str)
        num = 0
        while i < length and str[i] >= '0' and str[i] <= '9':
            num = num * 10 + int(str[i])
            i += 1
        num *= sign
        if num > 2 ** 31 - 1:
            num = 2 ** 31 - 1
        if num < - 2 ** 31:
            num = - 2 ** 31
        return num