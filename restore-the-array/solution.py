from functools import cache

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache
        def rec(i: int) -> int:
            if len(s) <= i:
                return 1
            if s[i] == '0':
                return 0
            res = 0
            for j in range(i + 1, len(s) + 1):
                if not (1 <= int(s[i:j]) <= k):
                    break
                res += 1 * rec(j)
            return res % 1_000_000_007

        return rec(0)