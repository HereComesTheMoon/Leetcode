class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        n = len(s1)
        d = defaultdict(int)
        for k in range(n):
            d[s2[k]] += 1
        for k in range(n):
            d[s1[k]] -= 1
            if d[s1[k]] == 0:
                del d[s1[k]]
        if not d:
            return True
        for k in range(n, len(s2)):
            d[s2[k]] += 1
            if d[s2[k]] == 0:
                del d[s2[k]]
            d[s2[k - n]] -= 1
            if d[s2[k - n]] == 0:
                del d[s2[k - n]]
            if not d:
                return True
        return False



        