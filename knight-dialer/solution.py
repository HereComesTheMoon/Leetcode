class Solution:
    def knightDialer(self, n: int) -> int:
        if n <= 6:
            return [0, 10, 20, 46, 104, 240, 544][n]

        if n % 2:
            a = 46
            b = 240
        else:
            a = 104
            b = 544

        for k in range((n-5)//2):
            a, b = b, 6 * b - 4 * a
        return b % 1_000_000_007