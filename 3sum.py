class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        if len(num) < 3:
            return []
        res = []
        for i in range(len(num) - 2):
            if i > 0 and num[i] == num[i - 1]:
                continue
            p = i + 1
            q = len(num) - 1
            while p < q:
                a = num[p]
                b = num[q]
                sum = a + b
                if sum == -num[i]:
                    res.append([num[i], a, b])
                    while p < q and a == num[p]:
                        p += 1
                    while q > p and b == num[q]:
                        q -= 1
                elif sum < -num[i]:
                    p += 1
                else:
                    q -= 1
        return res