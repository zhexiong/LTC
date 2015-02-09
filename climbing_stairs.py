    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 3:
            return n
        c1 = 1
        c2 = 2
        for i in range(3, n + 1):
            c3 = c1 + c2
            c1 = c2
            c2 = c3
        return c3