import heapq as pq
from bisect import bisect_left
from math import ceil

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = [None for _ in spells]
        for k, x in enumerate(spells):
            pos = bisect_left(potions, math.ceil(success / x))
            res[k] = len(potions) - pos
        return res