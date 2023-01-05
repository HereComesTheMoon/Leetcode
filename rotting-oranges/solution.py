EMPTY = 0
OKAY = 1
ROTTEN = 2

DIRS = [
    (1, 0),
    (-1,0),
    (0,1),
    (0,-1),
]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # (time, x, y), rotten
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == ROTTEN:
                    q.append((0, x, y))

        time = 0
        while q:
            t, x, y = q.popleft()
            time = t

            for xx, yy in DIRS:
                if y + yy not in range(len(grid)):
                    continue
                if x + xx not in range(len(grid[0])):
                    continue
                if grid[y + yy][x + xx] != OKAY:
                    continue
                q.append((t + 1, x + xx, y + yy))
                grid[y + yy][x + xx] = ROTTEN

        for row in grid:
            for val in row:
                if val == OKAY:
                    return -1
        return time