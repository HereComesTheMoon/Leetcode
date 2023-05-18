from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        if isqrt(n)**2 == n:
            return 1
        dp = [k for k in range(n + 1)]
        for k in range(isqrt(n) + 1):
            dp[k**2] = 1
        for k in range(n + 1):
            j = k + 1
            step = 3
            while j <= n:
                dp[j] = min(dp[j], dp[k] + 1)
                j += step
                step += 2
        return dp[-1]
