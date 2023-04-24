import heapq as pq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for k in range(len(stones)):
            stones[k] = - stones[k]
        pq.heapify(stones)
        while 2 <= len(stones):
            a = pq.heappop(stones)
            b = pq.heappop(stones)
            if b == a:
                continue
            pq.heappush(stones, a - b)
        if stones:
            return -stones[0]
        else:
            return 0