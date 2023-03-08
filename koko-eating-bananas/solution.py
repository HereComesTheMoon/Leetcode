class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a = 1
        b = max(piles)

        def check(speed: int) -> bool:
            time = sum( 1 + (pile - 1) // speed for pile in piles )
            return time <= h

        while a < b:
            mid = (a + b) // 2
            if check(mid):
                b = mid
            else:
                a = mid + 1
        return a