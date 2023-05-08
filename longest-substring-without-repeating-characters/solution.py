class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i = 0
        j = 1
        seen = { s[i] }
        res = 0
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            j += 1
            res = max(res, j - i)
        return res

