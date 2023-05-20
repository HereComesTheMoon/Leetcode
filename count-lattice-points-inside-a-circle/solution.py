class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        seen = set()
        for [xx, yy, r] in circles:
            for x in range(-r, r+1):
                for y in range(-r, r+1):
                    if x**2 + y**2 <= r**2:
                        seen.add((xx-x, yy-y))
        return len(seen)
