from copy import copy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [ [x] for x in range(1, n + 1) ]
        res = [list(range(1, k + 1))]
        while res[-1][0] != n + 1 - k:
            res.append(get_next(res[-1], n))
        return res


def get_next(comb: List[int], n: int) -> List[int]:
    j = len(comb) - 1
    i = 0
    comb = copy(comb)
    while comb[j - i] == n - i:
        i += 1
    comb[j - i] += 1
    i -= 1
    while 0 <= i:
        comb[j - i] = comb[j - i - 1] + 1
        i -= 1
    return comb


        