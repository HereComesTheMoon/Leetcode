class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        triple, middle, corner, zero = 3, 2, 2, 2
        for n in range(2, n):
            triple, middle, corner, zero = zero + 2 * corner, 2 * corner, middle + triple, 2 * triple

        return (2 * (triple + middle + 2 * corner) + zero) % 1_000_000_007
