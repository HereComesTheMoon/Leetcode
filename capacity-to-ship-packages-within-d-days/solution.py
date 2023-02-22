class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def passes(cap: int) -> bool:
            shipments = 0
            container = 0 
            for weight in weights:
                container += weight
                if cap < container:
                    shipments += 1
                    container = weight
            return days <= shipments
        
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            if passes(mid):
                l = mid + 1
            else:
                r = mid
        return l


