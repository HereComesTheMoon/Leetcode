class DSU:
    def __init__(self, xx: int, yy: int):
        self.d = [ [ None for x in range(xx) ] for y in range(yy) ]
        self.w = [ [ 1 for x in range(xx) ] for y in range(yy) ]

    def flood(self, x, y):
        self.d[y][x] = (x, y)
        merged = 0
        for xx in (-1,0,1):
            xx = x + xx
            for yy in (-1,0,1):
                yy = y + yy
                if not(0 <= xx < len(self.d[0])):
                    continue
                if not(0 <= yy < len(self.d)):
                    continue
                if self.d[yy][xx] is None:
                    continue
                self.merge(x, y, xx, yy)
                merged += 1
        return 2 <= merged or x == 0 or x == len(self.d[0]) - 1
    
    def check(self) -> bool:
        left = set()
        right = set()
        n = len(self.d[0]) - 1
        for y in range(len(self.d)):
            if self.d[y][0] is not None:
                left.add(self.get(self.d[y][0][0], self.d[y][0][1]))
            if self.d[y][n] is not None:
                right.add(self.get(self.d[y][n][0], self.d[y][n][1]))
        return bool(left & right)



    def get(self, x, y):
        while (x, y) != self.d[y][x]:
            xx, yy = self.d[y][x]
            self.d[y][x] = self.d[yy][xx]
            x, y = xx, yy
        return x, y

    def merge(self, px, py, qx, qy):
        px, py = self.get(px, py)
        qx, qy = self.get(qx, qy)
        if px == qx and py == qy:
            return (px, py)
        if self.w[qy][qx] <= self.w[py][px]:
            self.w[py][px] += self.w[qy][qx]
            self.d[qy][qx] = (px, py)
            return (px, py)
        else:
            self.w[qy][qx] += self.w[py][px]
            self.d[py][px] = (qx, qy)
            return (qx, qy)


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(col, row)
        for steps, (y, x) in enumerate(cells):
            check = dsu.flood(x-1, y-1)
            if check and dsu.check():
                return steps

