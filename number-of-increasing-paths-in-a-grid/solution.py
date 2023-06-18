class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        paths = [
            [None for val in row] for row in grid
        ]
        m = len(grid)
        n = len(grid[0])
        MOD = 1_000_000_007
        
        def rec(x: int, y: int):
            if paths[y][x] is not None:
                return paths[y][x]
            res = 1
            for xx, yy in ((1,0), (-1,0), (0,1), (0,-1)):
                xx = x + xx
                yy = y + yy
                if not(0 <= xx < n):
                    continue
                if not(0 <= yy < m):
                    continue
                if grid[yy][xx] <= grid[y][x]:
                    continue
                res += rec(xx, yy)
            paths[y][x] = res % MOD
            return res % MOD
        
        res = 0
        for y in range(m):
            for x in range(n):
                res += rec(x, y)
        return res % MOD
