from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        q = deque([(0, 0)])
        grid[0][0] = 1
        steps = 1
        while q:
            steps += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for yy in (1, 0, -1):
                    for xx in (1, 0, -1):
                        if not (0 <= y+yy < n):
                            continue
                        if not (0 <= x+xx < m):
                            continue
                        if 0 < grid[y + yy][x + xx]:
                            continue
                        grid[y+yy][x+xx] = steps
                        q.append((x+xx, y+yy))
        return grid[-1][-1] if grid[-1][-1] != 0 else -1


