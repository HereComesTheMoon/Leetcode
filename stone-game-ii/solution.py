class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        x = 0
        cumPiles = [0] + [ x := x + val for val in piles ]

        @functools.cache
        def rec(i, M, turn):
            if turn:
                res = 0
                for x in range(min(2*M, len(piles) - i)):
                    val = cumPiles[i + x + 1] - cumPiles[i]
                    res = max(
                        res,
                        val + rec(i + x + 1, max(M, x + 1), False)
                    )
            else:
                res = 1000000
                for x in range(min(2*M, len(piles) - i + 1)):
                    res = min(
                        res,
                        rec(i + x + 1, max(M, x + 1), True)
                    )
            return res

        return rec(0, 1, True)
