class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        res = [None for _ in questions]
        res[-1] = questions[-1][0]
        for k in reversed(range(n - 1)):
            bp = questions[k][1] + 1
            if k + bp < n:
                res[k] = max(res[k+1], questions[k][0] + res[k + bp])
            else:
                res[k] = max(res[k+1], questions[k][0])
        print(res)
        return res[0]