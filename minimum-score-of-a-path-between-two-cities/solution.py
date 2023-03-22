class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        out_roads = [[] for _ in range(n + 1)]
        for [a, b, length] in roads:
            out_roads[a].append((b, length))
            out_roads[b].append((a, length))
        seen = { 1 }
        process = [1]
        res = float('inf')
        while process:
            now = process.pop()
            for b, length in out_roads[now]:
                res = min(res, length)
                if b in seen:
                    continue
                seen.add(b)
                process.append(b)

        return res
