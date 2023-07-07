class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        for val in ('T', 'F'):
            i = 0
            j = 0
            kk = k
            while j < len(answerKey):
                if answerKey[j] == val:
                    j += 1
                    res = max(res, j - i)
                    continue
                if kk == 0:
                    kk += answerKey[i] != val
                    i += 1
                    continue
                j += 1
                kk -= 1
                res = max(res, j - i)
            res = max(res, j - i)
        return res