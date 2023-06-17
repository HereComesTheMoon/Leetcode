from bisect import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = [key for key, _ in itertools.groupby(sorted(arr2))]

        @functools.cache
        def rec(i: int, last: int):
            if i == len(arr1):
                return 0
            k = bisect(arr2, last)
            swap = 1 + rec(i+1, arr2[k]) if k < len(arr2) else math.inf
            noswap = rec(i+1, arr1[i]) if last < arr1[i] else math.inf
            return min(swap, noswap)
        res = rec(0, -math.inf)
        return -1 if res == math.inf else res
