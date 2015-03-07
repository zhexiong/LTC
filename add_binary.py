class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        res = ''
        while i >= 0 or j >=0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
            if j >= 0:
                sum += int(b[j])
            carry = sum / 2
            res = str(sum % 2) + res
            i -= 1
            j -= 1
        return str(carry) + res if carry else res