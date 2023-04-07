class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        yy = len(grid)
        xx = len(grid[0]) 
        def rec(y, x) -> int:
            if not 0 <= y < yy:
                return 0
            if not 0 <= x < xx:
                return 0
            if grid[y][x] == 0:
                return 0
            grid[y][x] = 0
            return 1 + rec(y+1, x) + rec(y-1, x) + rec(y, x+1) + rec(y, x-1)
        for y in range(yy):
            rec(y, 0)
            rec(y, xx-1)
        for x in range(xx):
            rec(0, x)
            rec(yy-1, x)
        total = 0
        for y in range(yy):
            for x in range(xx):
                total += rec(y, x)
        return total