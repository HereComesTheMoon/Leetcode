import heapq as pq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for x in tasks:
            d[x] = d.get(x, 0) + 1
        heap = [(0, -count) for count in d.values()]
        pq.heapify(heap)
        time = -1
        while heap:
            time += 1
            if time < heap[0][0]:
                continue
            while heap[0][0] < time:
                pq.heapreplace(heap, (time, heap[0][1]))
            if -heap[0][1] == 1:
                pq.heappop(heap)
                continue
            pq.heapreplace(heap, (time + n + 1, heap[0][1] + 1))
        return time + 1