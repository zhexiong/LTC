class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dl_map = {"1":["1"], "2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"], "0":[" "]}
        combs = []
        self.__letterCombinations(digits, 0, [], combs, dl_map)
        return combs
        
    def __letterCombinations(self, digits, index, comb, combs, dl_map):
        if index == len(digits):
            combs.append("".join(comb))
            return
        for letter in dl_map[digits[index]]:
            comb.append(letter)
            self.__letterCombinations(digits, index + 1, comb, combs, dl_map)
            comb.pop()