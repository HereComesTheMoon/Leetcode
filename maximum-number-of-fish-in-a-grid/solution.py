class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0

        def rec(x: int, y: int) -> int:
            if not(0 <= y < len(grid)):
                return 0
            if not(0 <= x < len(grid[0])):
                return 0
            if grid[y][x] == 0:
                return 0
            res = grid[y][x]
            grid[y][x] = 0
            for xx, yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                res += rec(x + xx, y + yy)
            return res

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                res = max(res, rec(x, y))
        
        return res