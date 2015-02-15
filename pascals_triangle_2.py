class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        current = [1]
        for i in range(1, rowIndex + 1):
            next = []
            next.append(1)
            for j in range(len(current) - 1):
                next.append(current[j] + current[j + 1])
            next.append(1)
            current = next
        return current