class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = 1 + high - low
        if n % 2 == 0:
            return n // 2
        return n // 2 + low % 2
        