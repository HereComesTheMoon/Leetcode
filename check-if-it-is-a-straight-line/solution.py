class Solution:
    def checkStraightLine(self, pts: List[List[int]]) -> bool:
        if pts[0][1] - pts[1][1] == 0:
            return all(pt[1] == pts[0][1] for pt in pts)
        a = (pts[1][0] - pts[0][0]) / (pts[1][1] - pts[0][1])
        b = pts[0][0] - a * pts[0][1]

        return all(abs(a*y + b - x) < 0.0000001 for [x, y] in pts)
