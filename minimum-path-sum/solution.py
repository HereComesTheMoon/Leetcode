import heapq as pq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        heap = [
            (grid[0][0], 0, 0)
        ]
        seen = set()
        while heap:
            weight, x, y = pq.heappop(heap)
            if (x, y) in seen:
                continue
            if x == len(grid[0]) - 1 and y == len(grid) - 1:
                return weight
            seen.add((x, y))

            if y < len(grid) - 1:
                pq.heappush(heap, (weight + grid[y + 1][x], x, y + 1))
            if x < len(grid[0]) - 1:
                pq.heappush(heap, (weight + grid[y][x + 1], x + 1, y))
        return -1
