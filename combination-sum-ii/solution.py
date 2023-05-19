from functools import cache

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        @cache
        def rec(i: int, target: int) -> list[int]:
            if target == 0:
                return ((),)
            if len(candidates) <= i or target < candidates[i]:
                return ()
            res = set()
            for x in rec(i + 1, target - candidates[i]):
                res.add((candidates[i],) + x)
            for x in rec(i + 1, target):
                res.add(x)
            return res

        return list(rec(0, target))

