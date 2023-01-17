class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        return ternary_search(lambda k: break_k(n, k), 2, n)


def break_k(n: int, k: int) -> int:
    b = n // k
    return  pow(b + 1, n % k) * pow(b, k - (n % k))


def ternary_search(f: Callable[[int], int], i: int, j: int) -> int:
    while i < j - 2:
        ii = i + (j - i) // 3
        jj = j - (j - i) // 3

        if f(ii) < f(jj):
            i = ii
        else:
            j = jj
    return max(f(k) for k in range(i, j + 1))
