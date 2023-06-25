class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1_000_000_007
        @functools.cache
        def rec(pos: int, fuel: int):
            now = locations[pos]
            res = int(pos == finish)
            if fuel < abs(locations[finish] - now):
                return res
            for x in itertools.chain(range(pos), range(pos+1, len(locations))):
                cost = abs(locations[x] - now)
                if fuel < cost:
                    continue
                res += rec(x, fuel - cost)
            
            return res % MOD

        return rec(start, fuel) % MOD