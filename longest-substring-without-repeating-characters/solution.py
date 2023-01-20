class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i = 0
        seen = { s[0] }
        res = 1
        for j in range(1, len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                res = max(res, j + 1 - i)
                continue
            while s[i] != s[j]:
                seen.remove(s[i])
                i += 1
            i += 1
        
        return res
            

            