class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [[] for _ in range(10)]
        w = str(num)
        for k, c in enumerate(w):
            digits[int(c)].append(k)
        for i, c in enumerate(w):
            for k in range(9, int(c), -1):
                if digits[k] and i < digits[k][-1]:
                    digs = list(w)
                    digs[i] = w[digits[k][-1]]
                    digs[digits[k][-1]] = c
                    return int("".join(digs))
        return num