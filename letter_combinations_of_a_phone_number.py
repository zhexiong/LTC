"""
Time: product of choices for each digits, n1 * n2 * n3 ...
Space: 
"""

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        map = {"1":"1", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "0":""}
        combs = []
        def helper(digits, index, comb, combs, map):
            if index == len(digits):
                combs.append(comb)
                return
            for l in map[digits[index]]:
                helper(digits, index + 1, comb + l, combs, map)
        helper(digits, 0, '', combs, map)
        return combs

class Solution2:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dl_map = {"1":"1", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "0":""}
        combs = [""]
        for num in digits:
            combs = [x + y for x in combs for y in dl_map[num]]
        return combs

if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations('23')