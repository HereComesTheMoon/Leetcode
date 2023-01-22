import heapq as pq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for x in tasks:
            d[x] = d.get(x, 0) + 1
        heap = [[0, -count] for count in d.values()]
        pq.heapify(heap)
        time = -1
        while heap:
            time += 1
            for x in heap:
                x[0] = max(x[0], time)
            if time < heap[0][0]:
                continue
            pq.heapify(heap)
            if -heap[0][1] == 1:
                pq.heappop(heap)
                continue
            pq.heapreplace(heap, [time + n + 1, heap[0][1] + 1])
        return time + 1