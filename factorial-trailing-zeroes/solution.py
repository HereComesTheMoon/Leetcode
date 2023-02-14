class Solution:
    def trailingZeroes(self, n: int) -> int:
        counter = 0
        p = 5
        while p <= n:
            counter += n // p
            p *= 5
        return counter

