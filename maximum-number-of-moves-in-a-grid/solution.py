from functools import cache

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def rec(i: int, j: int) -> int:
            if j == n - 1:
                return 0
            res = 0
            if 0 < i and grid[i][j] < grid[i - 1][j + 1]:
                res = max(res, 1 + rec(i - 1, j + 1))
            if grid[i][j] < grid[i][j + 1]:
                res = max(res, 1 + rec(i, j + 1))
            if i < m - 1 and grid[i][j] < grid[i + 1][j + 1]:
                res = max(res, 1 + rec(i + 1, j + 1))
            return res
        

        return max(rec(i, 0) for i in range(m))