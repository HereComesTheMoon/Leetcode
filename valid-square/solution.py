from itertools import combinations

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist_squared(px, py, qx, qy) -> int:
            return (px - qx)**2 + (py - qy)**2
        
        counter = defaultdict(int)
        for (px, py), (qx, qy) in combinations([p1, p2, p3, p4], 2):
            if (px, py) == (qx, qy):
                return False
            counter[dist_squared(px, py, qx, qy)] += 1
        
        return set(counter.values()) == { 4, 2 }
