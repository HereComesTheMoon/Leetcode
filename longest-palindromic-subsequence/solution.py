from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return rec(s)

@cache
def rec(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    if s[0] == s[-1]:
        return 2 + rec(s[1:len(s)-1])
    return max(rec(s[1:]), rec(s[:len(s)-1]))