class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        start = 0
        end = x
        while start <= end:
            mid = (start + end) / 2
            temp = mid ** 2
            if temp == x:
                return mid
            elif temp > x:
                end = mid - 1
            else:
                start = mid + 1
        return (start + end) / 2

def sqrt_float(x):
    low = 0
    high = max(1.0, x)
    prec = 0.0001
    while low < high:
        mid = (low + high) / 2.0
        if abs(mid * mid - x) < prec:
            return mid
        elif mid * mid > x:
            high = mid
        else:
            low = mid
    return (low + high) / 2.0