class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        edg_in = [ set() for k in range(n) ]
        edg_out = [ set() for k in range(n) ]
        for [a, b] in edges:
            edg_out[a].add(b)
            edg_in[b].add(a)
        todo = set()
        for k in range(n):
            if not edg_in[k]:
                todo.add(k)
        total = 0
        inc_paths = [ { colors[k] : 1 } for k in range(n) ]

        while todo:
            now = todo.pop()
            total += 1
            assert not edg_in[now]
            for x in edg_out[now]:
                edg_in[x].remove(now)
                if not edg_in[x]:
                    todo.add(x)
                for color in inc_paths[now]:
                    inc_paths[x][color] = max(inc_paths[x].get(color, 0), inc_paths[now][color])
                col_x = colors[x]
                inc_paths[x][col_x] = max(inc_paths[x][col_x], 1 + inc_paths[now].get(col_x, 0))
            print(now, inc_paths[now])

        largest = 0
        if total != len(colors):
            return -1
        for k in range(n):
            for val in inc_paths[k].values():
                largest = max(largest, val)
        return largest







