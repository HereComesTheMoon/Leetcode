class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        todo = set(range(n))
        nums = []
        while todo:
            stack = [todo.pop()]
            num = 0
            while stack:
                now = stack.pop()
                num += 1
                todo.discard(now)
                for x in graph[now]:
                    if x not in todo:
                        continue
                    stack.append(x)
                    todo.discard(x)
            nums.append(num)
        return sum(x * (n - x) for x in nums) // 2