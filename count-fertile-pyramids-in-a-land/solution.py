from pprint import pprint

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        grid = [[0] * (m+2)]+ [ [0] + row + [0] for row in grid ] + [[0] * (m+2)]

        @functools.cache
        def rec(i, j, flipped):
            if grid[i+1][j] == 0:
                return grid[i][j] == 1
            if grid[i][j] == 0:
                return 0
            return 1 + min(rec(i+1,j-1, flipped), rec(i+1,j+1, flipped))

        res = 0
        for y in range(1, n):
            for x in range(1, m):
                res += max(0, rec(y, x, True) - 1)
        
        grid.reverse()
        for y in range(1, n):
            for x in range(1, m):
                res += max(0, rec(y, x, False) - 1)

        return res
