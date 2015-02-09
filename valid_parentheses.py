class Solution:
    # @return a boolean
    def isValid(self, s):
        leftStack = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                leftStack.append(p)
            else:
                if len(leftStack) == 0:
                    return False
                left = leftStack.pop()
                if p == ')' and left != '(':
                    return False
                elif p == ']' and left != '[':
                    return False
                elif p == '}' and left != '{':
                    return False
        if len(leftStack) == 0:
            return True
        return False