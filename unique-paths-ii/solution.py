class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        @functools.cache
        def path(x: int, y: int) -> int:
            if not(0 <= y < len(grid)):
                return 0
            if not(0 <= x < len(grid[0])):
                return 0
            if grid[y][x]:
                return 0
            if y == len(grid) -1 and x == len(grid[0]) - 1:
                return 1
            return sum(path(x + xx, y + yy) for (xx, yy) in [(1,0), (0,1)])
        
        return path(0, 0)