from functools import cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        @cache
        def rec(bound: int) -> int:
            if bound <= 0:
                return 1
            return (rec(bound - zero) + rec(bound - one)) % 1_000_000_007
            
        return (rec(high + 1) - rec(low)) % 1_000_000_007