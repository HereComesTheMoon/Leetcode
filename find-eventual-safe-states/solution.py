class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()
        not_safe = set()
        seen = set()

        def rec(x: int) -> bool:
            if x in safe:
                return True
            if x in not_safe or x in seen:
                return False
            seen.add(x)
            if all(rec(y) for y in graph[x]):
                safe.add(x)
                seen.remove(x)
                return True
            else:
                not_safe.add(x)
                return False
        
        for x, _ in enumerate(graph):
            rec(x)
        
        return sorted(list(safe))