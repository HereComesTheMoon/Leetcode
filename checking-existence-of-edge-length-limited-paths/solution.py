class DSU: 
    def __init__(self, n: int):
        self.d = list(range(n))
        self.weights = [1 for _ in range(n)]

    def get(self, x: int) -> int:
        while self.d[x] != x:
            self.d[x] = self.d[self.d[x]]
            x = self.d[x]
        return x
    
    def merge(self, a: int, b: int) -> int:
        a = self.get(a)
        b = self.get(b)
        if a == b:
            return
        if self.weights[a] < self.weights[b]:
            self.weights[b] += self.weights[a]
            self.d[a] = b
        else:
            self.weights[a] += self.weights[b]
            self.d[b] = a


class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges.sort(reverse=True, key=lambda row: row[2])

        queries = [ (limit, start, goal, k) for k, [start, goal, limit] in enumerate(queries) ]
        queries.sort()

        dsu = DSU(n)

        results = [None for _ in range(len(queries))]

        for limit, start, goal, k in queries:
            while edges and edges[-1][2] < limit:
                u, v, dis = edges.pop()
                dsu.merge(u, v)
            results[k] = dsu.get(start) == dsu.get(goal)
        return results
