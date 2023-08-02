class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        neighbours = [(1,0),(-1,0),(0,1),(0,-1)]
        def rec(x, y, seen):
            if not(0 <= y < len(grid)):
                return 0
            if not(0 <= x < len(grid[0])):
                return 0
            if grid[y][x] == 0:
                return 0
            if (x, y) in seen:
                return 0
            seen.add((x, y))
            res = grid[y][x] + max(rec(x + xx, y + yy, seen) for xx, yy in neighbours)           
            seen.remove((x, y))
            return res
        
        res = 0
        seen = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                res = max(res, rec(x, y, seen))
        return res