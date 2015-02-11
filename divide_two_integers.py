class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        max_int = 2 ** 31 - 1
        if divisor == 0:
            return max_int
        if dividend == 0:
            return 0
        sign = -1 if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0 else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            k = 0
            while dividend >= (divisor << k):
                k += 1
            dividend -= divisor << (k - 1)
            result += 1 << (k - 1)
        return sign * result if sign * result < max_int else max_int