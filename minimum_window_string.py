class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) == 0 or len(S) < len(T):
            return ""
        missing = {}
        found = {}
        for ch in T:
            if ch in missing:
                missing[ch] += 1
            else:
                missing[ch] = 1
        minWin = len(S) + 1
        ans = ""
        start = 0
        count = 0
        for i in range(len(S)):
            if S[i] in missing:
                if S[i] in found:
                    found[S[i]] += 1
                else:
                    found[S[i]] = 1
                if found[S[i]] <= missing[S[i]]:
                    count += 1
            if count == len(T):
                while start <= i:
                    if S[start] in missing:
                        if found[S[start]] > missing[S[start]]:
                            found[S[start]] -= 1
                        else:
                            break
                    start += 1
                if minWin > i - start + 1:
                    minWin = i - start + 1
                    ans = S[start : i + 1]
        return ans