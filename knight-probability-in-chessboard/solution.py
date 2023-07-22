steps = [
    (1,2),
    (-1,2),
    (1,-2),
    (-1,-2),
    (2,1),
    (-2,1),
    (2,-1),
    (-2,-1),    
]

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        now = [ [0.] * n for _ in range(n) ]
        now[row][column] = 1.0
        for _ in range(k):
            new = [ [0.] * n for _ in range(n) ]
            for y in range(n):
                for x in range(n):
                    for xx, yy in steps:
                        if not(0 <= y + yy < n):
                            continue
                        if not(0 <= x + xx < n):
                            continue
                        new[y][x] += now[y + yy][x + xx] / 8.
            now = new
        return sum(x for row in now for x in row)