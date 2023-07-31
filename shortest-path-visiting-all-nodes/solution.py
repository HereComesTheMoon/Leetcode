class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        q = collections.deque(
            (x,) for x in range(len(graph))
        )
        steps = 0
        seen = set()
        while q:
            steps += 1
            for _ in range(len(q)):
                path = q.popleft()
                for nxt in graph[path[-1]]:
                    next_path = path + (nxt,)
                    check = frozenset(next_path)
                    if (nxt, check) in seen:
                        continue
                    seen.add((nxt, check))
                    if len(check) == len(graph):
                        return steps
                    q.append(next_path)
