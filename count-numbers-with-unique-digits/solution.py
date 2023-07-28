class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1
        for k in range(1, n + 1):
            val = 9
            for i in range(k - 1):
                val *= (9 - i)
            res += val
        return res