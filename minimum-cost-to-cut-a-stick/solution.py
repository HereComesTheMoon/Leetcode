class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @functools.cache
        def rec(i: int, j: int) -> int:
            if j <= i + 1:
                return 0
            res = float('inf')
            ii = bisect.bisect(cuts, i)
            jj = bisect.bisect_left(cuts, j)
            if jj <= ii:
                return 0
            for k, x in enumerate(cuts[ii:jj], ii):
                l = rec(i, x)
                r = rec(x, j)
                res = min(res, l + r)
            return res + (j - i)
        
        return rec(0, n)
                

