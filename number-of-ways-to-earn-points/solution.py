class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 1_000_000_007

        @functools.cache
        def rec(pos: int, target: int) -> int:
            if target <= 0:
                return target == 0
            if pos == len(types):
                return 0
            [count, marks] = types[pos]
            return sum(rec(pos + 1, target - marks * x) for x in range(count + 1)) % MOD
        
        return rec(0, target) % MOD