class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        result = ''
        arr = path.split('/')
        stack = []
        for p in arr:
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            elif p == '.' or not p:
                pass
            else:
                stack.append(p)
        return '/' + '/'.join(stack)