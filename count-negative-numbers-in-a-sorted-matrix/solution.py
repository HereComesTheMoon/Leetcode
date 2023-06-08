class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(grid[y][x] < 0 for y in range(len(grid)) for x in range(len(grid[0])))