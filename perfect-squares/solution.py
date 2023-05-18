from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [k**2 for k in range(1, isqrt(n) + 1)]
        frontier = { 0 }
        steps = 0
        while True:
            steps += 1
            frontier = { x + square for square in squares for x in frontier }
            if n in frontier:
                return steps

