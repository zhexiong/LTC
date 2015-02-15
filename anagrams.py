class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if len(strs) == 0:
            return []
        strHash = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in strHash:
                strHash[sorted_str].append(str)
            else:
                strHash[sorted_str] = [str]
        results = []
        for key in strHash:
            if len(strHash[key]) > 1:
                results.extend(strHash[key])
        return results