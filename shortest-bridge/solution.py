from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        seen = set()

        def check(x, y) -> bool:
            if (x, y) in seen:
                return True
            if y not in range(n):
                return True
            if x not in range(m):
                return True
            return False

        def rec(x, y):
            if check(x, y):
                return
            if grid[y][x] == 0:
                return
            seen.add((x,y))
            for xx, yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                rec(x+xx,y+yy)

        x, y = next(((x, y) for y in range(n) for x in range(m) if grid[y][x] == 1))
        rec(x, y)

        q = deque(seen)
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for xx, yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if check(x+xx, y+yy):
                        continue
                    if grid[y+yy][x+xx] == 1:
                        return steps
                    seen.add((x+xx, y+yy))
                    q.append((x+xx, y+yy))
            steps += 1


                


