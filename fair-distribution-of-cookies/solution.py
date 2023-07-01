class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = 1_000_000
        cookies.sort(reverse=True)
        def rec(pos: int, given: list[int]):
            maxi = max(given)
            nonlocal res
            if res <= maxi:
                return
            elif pos == len(cookies):
                res = min(res, maxi)
                return
            for i in range(k):
                given[i] += cookies[pos]
                rec(pos + 1, given)
                given[i] -= cookies[pos]
        
        rec(0, [0]*k)
        return res
