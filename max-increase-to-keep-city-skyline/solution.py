class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hy = [max(row) for row in grid]
        hx = [max(row[x] for row in grid) for x in range(n)]
        res = 0
        for y in range(n):
            for x in range(n):
                res += min(hy[y], hx[x]) - grid[y][x]
        return res

