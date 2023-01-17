class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        k = 0
        for x in t:
            if x == s[k]:
                k += 1
                if len(s) <= k:
                    return True
        return False