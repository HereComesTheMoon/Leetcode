import heapq as pq

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for [a, b] in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        seen = { 0 }
        def rec(k: int):
            res = 0
            for [x, cost] in graph[k]:
                if x in seen:
                    continue
                seen.add(x)
                res += cost
                res += rec(x)
            return res
        res = rec(0)
        return res

