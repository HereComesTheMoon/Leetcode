from functools import cache

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        left = list(range(1, n + 1))
        k = k - 1
        while left:
            i, k = divmod(k, factorial(len(left) - 1))
            res.append(str(left[i]))
            left.pop(i)

        return "".join(res)

@cache
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

