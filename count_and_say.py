class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        ans = '1'
        i = 2
        while i <= n:
            j = 0
            temp = ''
            while j < len(ans):
                start = j
                while j < len(ans) and ans[start] == ans[j]:
                    j += 1
                temp += str(j - start) + str(ans[start])
            ans = temp
            i += 1
        return ans