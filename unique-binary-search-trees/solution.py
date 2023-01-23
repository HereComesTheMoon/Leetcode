from functools import cache

class Solution:
    def numTrees(self, n: int) -> int:
        return catalan(n)


@cache
def catalan(n: int) -> int:
    if n <= 1:
        return 1
    return sum(catalan(n - 1 - i) * catalan(i) for i in range(n))