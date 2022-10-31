neighbours = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def delete_island(grid: List[List[str]], x: int, y: int):
            if grid[y][x] != "1":
                return
            
            grid[y][x] = "0"
            for xx, yy in ( (x + xx, y + yy) for xx, yy in neighbours ):
                if yy in range(len(grid)) and xx in range(len(grid[0])):
                    delete_island(grid, xx, yy)
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    delete_island(grid, x, y)
                    count += 1
        
        return count
                    