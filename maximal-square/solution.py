from math import isqrt

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        a = [ [ 0 for _ in range(m + 1) ] for _ in range(n+1) ]
        for y in range(1, n+1):
            for x in range(1, m+1):
                a[y][x] = a[y-1][x] + a[y][x-1] - a[y-1][x-1] + (matrix[y-1][x-1] == '1')
        
        res = int(a[-1][-1] != 0)
        for y in range(1, n + 1):
            for x in range(1, m + 1):
                for k in range(res, min(y, x) + 1):
                    box = a[y][x] - a[y-k][x] - a[y][x-k] + a[y-k][x-k]
                    if k ** 2 == box:
                        res = k
                    else:
                        break

        return res ** 2