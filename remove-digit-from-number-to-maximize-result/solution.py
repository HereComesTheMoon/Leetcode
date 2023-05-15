class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = 0
        for k, c in enumerate(number):
            if c == digit:
                res = max(res, int(number[:k] + number[k+1:]))
        return str(res)