import heapq as pq

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        heap = []
        seen = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    heap.append((0, x, y))
                    seen.add((x,y))
        
        if len(heap) == len(grid) * len(grid[0]):
            return -1
        while heap:
            dist, x, y = pq.heappop(heap)
            for [xx, yy] in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                xx = x + xx
                yy = y + yy
                if (xx, yy) in seen:
                    continue
                if not (0 <= xx < len(grid[0])):
                    continue
                if not (0 <= yy < len(grid)):
                    continue
                seen.add((xx, yy))
                pq.heappush(heap, (dist + 1, xx, yy))
            if not heap:
                return dist
            
        return -1
                