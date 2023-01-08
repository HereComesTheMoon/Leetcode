import heapq as h
import math

def norm(p: tuple[int, int]) -> float:
    return math.sqrt(p[0]**2 + p[1]**2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [ (norm(p), p) for p in points ]
        h.heapify(pq)
        return [ h.heappop(pq)[1] for _ in range(k) ]
            
