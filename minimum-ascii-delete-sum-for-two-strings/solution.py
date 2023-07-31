class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @functools.cache
        def rec(i: int, j: int) -> int:
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])
            if s1[i] == s2[j]:
                return rec(i + 1, j + 1)
            else:
                return min(
                    ord(s1[i]) + rec(i + 1, j),
                    ord(s2[j]) + rec(i, j + 1)
                )
        
        return rec(0, 0)