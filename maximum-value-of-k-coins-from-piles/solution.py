class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @functools.cache
        def rec(pile: int, left: int) -> int:
            if left == 0:
                return 0
            if len(piles) <= pile:
                return 0
            taken = 0
            res = rec(pile + 1, left)
            for i in range(min(left, len(piles[pile]))):
                taken += piles[pile][i]
                res = max(res, taken + rec(pile + 1, left - i - 1))
            return res

        return rec(0, k)
            
