class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    res += 4
                    for yy, xx in [(1,0), (-1,0), (0,1), (0,-1)]:
                        if y + yy in range(len(grid)) and x + xx in range(len(grid[0])):
                            res -= grid[y + yy][x + xx] == 1

        return res