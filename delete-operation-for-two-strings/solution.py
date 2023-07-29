class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        @functools.cache
        def rec(i, j):
            if len(w1) <= i or len(w2) <= j:
                return max(len(w1) - i, len(w2) - j)
            if w1[i] == w2[j]:
                return rec(i + 1, j + 1)
            return 1 + min(rec(i + 1, j), rec(i, j + 1))
        
        return rec(0, 0)