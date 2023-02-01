class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = prices[0]
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                continue
            profit += prices[i-1] - smallest
            smallest = prices[i]
        profit += prices[-1] - smallest
        return profit
