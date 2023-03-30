from collections import Counter
from functools import cache

class Solution:
    def isScramble(self, comp: str, s: str) -> bool:
        return rec(comp, s)

    
@cache
def rec(comp: str, s: str) -> bool:
    if Counter(comp) != Counter(s):
        return False
    if comp == s:
        return True
    for k in range(1, len(s)):
        if rec(comp[:k], s[:k]) and rec(comp[k:], s[k:]):
            return True
        if rec(comp[len(s) - k:], s[:k]) and rec(comp[:len(s) - k], s[k:]):
            return True
    return False
        