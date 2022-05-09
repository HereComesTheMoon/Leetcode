class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        a, b = 2, 3
        for k in range(3, n):
            a, b = b, a + b

        return b
