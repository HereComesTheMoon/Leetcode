class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res = []
        n = len(p)
        d = defaultdict(int)
        for k in range(n):
            d[p[k]] -= 1
        for k in range(n):
            d[s[k]] += 1
            if d[s[k]] == 0:
                del d[s[k]]
        if not d:
            res.append(0)
        for k in range(n, len(s)):
            d[s[k]] += 1
            if d[s[k]] == 0:
                del d[s[k]]
            d[s[k - n]] -= 1
            if d[s[k - n]] == 0:
                del d[s[k - n]]
            if not d:
                res.append(k + 1 - n)
        return res