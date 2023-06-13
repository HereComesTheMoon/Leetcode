class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        for i, row in enumerate(grid):
            for j in range(len(grid)):
                if all(grid[i][k] == grid[k][j] for k in range(len(grid))):
                    res += 1
        return res
