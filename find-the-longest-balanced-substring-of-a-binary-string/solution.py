class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        c0 = 0
        c1 = 0
        last = None
        for x in s:
            if x == last:
                if x == '0':
                    c0 += 1
                else:
                    c1 += 1
                    res = max(res, 2 * min(c1, c0))
            else:
                last = x
                if x == '0':
                    c1 = 0
                    c0 = 1
                else:
                    c1 = 1
                    res = max(res, 2 * min(c1, c0))
        return res