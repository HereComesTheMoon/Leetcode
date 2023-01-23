class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        needed = [-1 for _ in range(amount + 1)]
        needed[0] = 0
        for k in range(amount + 1):
            for coin in coins:
                if k < coin:
                    continue
                if needed[k - coin] == -1:
                    continue
                if needed[k] == -1:
                    needed[k] = needed[k - coin] + 1
                needed[k] = min(needed[k], needed[k - coin] + 1)
        return needed[amount]



