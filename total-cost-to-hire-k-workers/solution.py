import heapq as pq
from collections import deque

class Solution:
    def totalCost(self, costs: List[int], k: int, c: int) -> int:
        if len(costs) <= 2*c:
            return sum(list(sorted(costs))[:k])
        q = deque(costs[c:len(costs)-c])
        hl = costs[:c]
        pq.heapify(hl)
        hr = costs[-c:]
        pq.heapify(hr)

        res = 0
        for _ in range(k):
            if not hr or hl and hl[0] <= hr[0]:
                res += pq.heappop(hl)
                if q:
                    pq.heappush(hl, q.popleft())
            else:
                res += pq.heappop(hr)
                if q:
                    pq.heappush(hr, q.pop())

        return res
        