MOD = 1_000_000_007

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        vals = [0 for _ in range(forget)]
        vals[0] = 1
        for _ in range(n-1):
            vals = [0] + vals[:len(vals) - 1]
            vals[0] = sum(vals[delay:]) % MOD
        return sum(vals) % MOD
