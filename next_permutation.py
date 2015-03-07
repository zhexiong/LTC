class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) == 0:
            return num
        last = num[len(num) - 1]
        i = len(num) - 2
        while i >= 0:
            if num[i] < last:
                j = len(num) - 1
                while j >= i and num[i] >= num[j]:
                    j -= 1
                num[j], num[i] = num[i], num[j]
                self.reverse(num, i + 1, len(num) - 1)
                break
            elif i == 0:
                self.reverse(num, i, len(num) - 1)
            last = num[i]
            i -= 1
        return num
        
    def reverse(self, num, i, j):
        while i <= j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1