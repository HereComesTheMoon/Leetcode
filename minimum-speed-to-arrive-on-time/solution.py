class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour + 1 <= len(dist):
            return -1
        def check(v: int) -> bool:
            val = 0
            for x in dist:
                val = math.ceil(val)
                val += x / v
            return val <= hour
        
        a = 1
        b = 10_000_001
        while a < b:
            mid = (a + b) // 2
            if check(mid):
                b = mid
            else:
                a = mid + 1
        return a