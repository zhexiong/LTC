class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) < 2:
            return True
        start = 0
        end = len(s) - 1
        while start <= end:
            while start <= end and not re.match('[a-z0-9]', s[start].lower()):
                start += 1
            while end >= start and not re.match('[a-z0-9]', s[end].lower()):
                end -= 1
            if start <= end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True