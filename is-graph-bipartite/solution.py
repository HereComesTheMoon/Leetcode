class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) <= 2:
            return True
        todo = { x for x in range(len(graph)) }
        left = set()
        right = set()
        
        def rec(vertex: int, left_side: bool) -> bool:
            if left_side:
                if vertex in left:
                    return True
                if vertex in right:
                    return False
                left.add(vertex)
                todo.remove(vertex)
                return all(rec(x, False) for x in graph[vertex])
            else:
                if vertex in right:
                    return True
                if vertex in left:
                    return False
                right.add(vertex)
                todo.remove(vertex)
                return all(rec(x, True) for x in graph[vertex])
        
        while len(left) + len(right) < len(graph):
            new_vertex = todo.pop()
            todo.add(new_vertex)
            if rec(new_vertex, True):
                continue
            return False
        return True