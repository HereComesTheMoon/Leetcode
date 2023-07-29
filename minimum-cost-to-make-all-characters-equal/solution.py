class Solution:
    def minimumCost(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        cost = 0
        while i < j:
            while i < j and s[i] == s[i + 1]:
                i += 1
            while i < j and s[j] == s[j - 1]:
                j -= 1
            if j <= i:
                return cost
            if i + 1 < len(s) - j:
                cost += i + 1
                i += 1
            else:
                cost += len(s) - j
                j -= 1
        return cost