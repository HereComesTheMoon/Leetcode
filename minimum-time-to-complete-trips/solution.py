class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        a = 0
        b = min(time) * totalTrips

        def check(t: int) -> bool:
            return totalTrips <= sum(t // x for x in time)

        while a < b:
            mid = (a + b) // 2
            if check(mid):
                b = mid
            else:
                a = mid + 1
        return a
