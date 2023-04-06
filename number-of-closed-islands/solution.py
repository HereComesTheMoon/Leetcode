class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def rec(x: int, y: int):
            if not 0 <= y < len(grid):
                return
            if not 0 <= x < len(grid[0]):
                return
            if grid[y][x] == 1:
                return
            grid[y][x] = 1
            rec(x + 1, y)
            rec(x - 1, y)
            rec(x, y + 1)
            rec(x, y - 1)

        for y in range(len(grid)):
            rec(0, y)
            rec(len(grid[0]) - 1, y)
        for x in range(len(grid[0])):
            rec(x, 0)
            rec(x, len(grid) - 1)

        total = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    total += 1
                    rec(x, y)
        return total