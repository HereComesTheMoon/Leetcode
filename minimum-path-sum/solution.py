import heapq as pq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        heap: List[(int, (int, int))] = [(grid[0][0], (0, 0))]
        seen = set()
        while True:
            weight, (x, y) = pq.heappop(heap)
            if x == len(grid[0]) - 1 and y == len(grid) - 1:
                return weight
            if x + 1 < len(grid[0]) and (x+1, y) not in seen:
                pq.heappush(heap, (weight + grid[y][x+1], (x + 1, y)))
                seen.add((x+1, y))
            if y + 1 < len(grid) and (x, y+1) not in seen:
                pq.heappush(heap, (weight + grid[y+1][x], (x, y + 1)))
                seen.add((x, y+1))
