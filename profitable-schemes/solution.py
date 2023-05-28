class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 1_000_000_007
        dp = [ [0] * (n + 1)  for _ in range(minProfit + 1) ]
        dp[0][0] = 1
        for prf, mem in zip(profit, group):
            dp_prev = copy.deepcopy(dp)
            for y in range(minProfit + 1):
                for x in range(n - mem + 1):
                    dp[min(minProfit, y + prf)][x + mem] += dp_prev[y][x] % MOD
                    
        return sum(dp[minProfit][x] for x in range(n + 1)) % MOD

