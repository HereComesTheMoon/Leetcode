from functools import cache

class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def rec(i: int, j: int) -> int:
            if j <= i:
                return 0
            if s[i] == s[j]:
                return rec(i + 1, j - 1)
            return 1 + min(rec(i+1, j), rec(i, j-1))
        return rec(0, len(s) - 1)

