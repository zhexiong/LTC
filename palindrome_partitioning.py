class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        partitions = []
        self.partitionHelper(s, 0, 0, [], partitions)
        return partitions
    
    def partitionHelper(self, s, start, end, partition, partitions):
        if start >= len(s):
            partitions.append(partition[:])
            return
        while end < len(s):
            if self.isPalindrome(s, start, end):
                partition.append(s[start:end + 1])
                self.partitionHelper(s, end + 1, end + 1, partition, partitions)
                partition.pop()
            end += 1
    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True