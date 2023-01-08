Hold = 0
Free = 1
Cool = 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        return dp(prices)


def dp(prices: List[int]) -> int:
    dd = [ [0, 0, 0] for _ in range(len(prices) + 1) ]
    dd[0] = [0, 0, 0]
    dd[1] = [-prices[0], 0, 0]
    for k in range(2, len(prices) + 1):
        dd[k][Hold] = max(dd[k-1][Hold], dd[k-1][Free] - prices[k-1])
        dd[k][Free] = max(dd[k-1][Cool], dd[k-1][Free])
        dd[k][Cool] = dd[k-1][Hold] + prices[k-1]
    print(dd)
    return max(dd[-1])