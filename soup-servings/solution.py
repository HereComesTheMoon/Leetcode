class Solution:
    def soupServings(self, n: int) -> float:
        if 10_000 < n:
            return 1.

        @functools.cache
        def rec(a: int, b: int) -> float:
            if a <= 0:
                if b <= 0:
                    return 0.5
                else:
                    return 1.
            if b <= 0:
                return 0.
            return sum(
                0.25 * rec(a - aa, b - bb) for aa, bb in [
                    (100,0),
                    (75,25),
                    (50,50),
                    (25,75),
                ]
            )
        return rec(n, n)
            