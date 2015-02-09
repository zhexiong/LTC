class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        result = [0, 1]
        for i in range(1, n):
            high = 1 << i
            rest = []
            for r in reversed(result):
                rest.append(high + r)
            result.extend(rest)
        return result