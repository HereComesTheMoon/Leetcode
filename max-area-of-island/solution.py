DIRS = [
    (1, 0),
    (-1,0),
    (0, 1),
    (0,-1),
]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                res = max(get_size(grid, x, y), res)
        return res
    

def get_size(grid: list[list[int]], x: int, y: int) -> int:
    if not 0 <= y < len(grid):
        return 0
    if not 0 <= x < len(grid[0]):
        return 0
    if grid[y][x] != 1:
        return 0
    grid[y][x] = 0
    res = 1
    for xx, yy in DIRS:
        res += get_size(grid, x + xx, y + yy)
    return res