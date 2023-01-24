from collections import defaultdict
import heapq as pq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        assert len(edges) == len(succProb)
        for k in range(len(edges)):
            adj[edges[k][0]].append((edges[k][1], succProb[k]))
            adj[edges[k][1]].append((edges[k][0], succProb[k]))

        heap = [(-1., start)]
        seen = set()

        while heap:
            val = pq.heappop(heap)
            prob = -val[0]
            vertex = val[1]
            if vertex in seen:
                continue
            if vertex == end:
                return prob
            seen.add(vertex)
            neighbours = adj[vertex]
            for adj_vertex, adj_prob in neighbours:
                if adj_vertex in seen:
                    continue
                pq.heappush(heap, (- prob * adj_prob, adj_vertex))

        return 0.
