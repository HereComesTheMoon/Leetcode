from functools import cache

MOD = 1_000_000_007

class Solution:
    def countHousePlacements(self, n: int) -> int:
        return (fib(n-2)**2 + 2*fib(n-1)*fib(n-2) + fib(n-1)**2) % MOD


@cache
def fib(n: int) -> int:
    if n <= 0:
        return 1
    return (fib(n - 1) + fib(n - 2)) % MOD