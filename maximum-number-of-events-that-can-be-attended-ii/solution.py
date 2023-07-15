class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        
        @functools.cache
        def rec(i: int, left: int):
            if left == 0:
                return 0
            if len(events) <= i:
                return 0
            [_, end, value] = events[i]
            next_i = bisect.bisect_left(events, end + 1, key=lambda l: l[0])
            return max(
                rec(i + 1, left),
                value + rec(next_i, left - 1)
            )
        
        return rec(0, k)