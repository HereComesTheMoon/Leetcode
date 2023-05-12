from functools import cache

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        @cache
        def rec(i: int) -> int:
            if len(questions) <= i:
                return 0
            return max(
                rec(i + 1),
                questions[i][0] + rec(i + 1 + questions[i][1])
            )

        return rec(0)