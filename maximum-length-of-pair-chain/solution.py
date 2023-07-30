class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        @functools.cache
        def rec(last: int, pos: int) -> int:
            if pos == len(pairs):
                return 0
            head, tail = pairs[pos]
            if head <= last:
                return rec(last, pos + 1)
            return max(
                rec(last, pos + 1),
                1 + rec(tail, pos + 1)
            )

        return rec(float('-inf'), 0)