from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        assert len(piles) <= h
        can_finish = lambda eating_speed: sum(ceil(pile_size / eating_speed) for pile_size in piles) <= h
        i = 1
        j = max(piles)
        while i < j:
            if can_finish((j + i) // 2):
                j = (j + i) // 2
            else:
                i = (j + i) // 2 + 1
        return i