class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        yes = -prices[0]
        no = 0
        for x in prices[1:]:
            temp_yes = yes
            yes = max(yes, no - x)
            no = max(no, temp_yes + (x - fee))
        return max(yes, no)