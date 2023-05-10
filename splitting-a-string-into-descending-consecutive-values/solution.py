class Solution:
    def splitString(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        def rec(s: str, val: int) -> bool:
            if int(s) == val - 1:
                return True
            for k in range(1, len(s)):
                num = int(s[:k])
                if num < val - 1:
                    continue
                if num == val - 1:
                    return rec(s[k:], val - 1)
                return False
            return False
            
        for i in range(1, len(s)):
            if rec(s[i:], int(s[:i])):
                return True
        return False