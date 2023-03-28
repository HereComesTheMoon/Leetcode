class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(366)]
        days = set(days)
        [day, week, month] = costs
        for t in range(366):
            if t in days:
                dp[t] = min(
                    day + dp[t-1],
                    week + dp[t - 7],
                    month + dp[t - 30]
                )
            else:
                dp[t] = dp[t-1]
        return dp[-1]