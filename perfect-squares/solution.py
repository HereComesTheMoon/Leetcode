from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [k**2 for k in range(1, isqrt(n) + 1)]
        squares.reverse()

        squares_check = set(squares)

        if n in squares_check:
            return 1
        @cache
        def rec(n: int) -> int:
            if n <= 1:
                return 1 if n == 1 else 0
            if n in squares_check:
                return 1
            val = float('inf')
            for x in squares:
                if n < x:
                    continue
                val = min(val, rec(n-x))
            return val + 1
        
        return rec(n)