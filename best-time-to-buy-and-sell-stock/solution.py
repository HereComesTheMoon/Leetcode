class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = prices[0]
        for x in prices[1:]:
            smallest = min(smallest, x)
            profit = max(profit, x - smallest)
        return profit