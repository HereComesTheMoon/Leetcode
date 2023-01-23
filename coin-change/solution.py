import heapq as pq

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        heap = [ (1, coin) for coin in coins ]
        seen = set(coins)
        while heap:
            num, val = pq.heappop(heap)
            for coin in coins:
                if val + coin == amount:
                    return num + 1
                if amount < val + coin:
                    continue
                if val + coin in seen:
                    continue
                seen.add(val + coin)
                pq.heappush(heap, (num + 1, val + coin))
        return -1
                
