class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        boss = defaultdict(list)
        for k, man in enumerate(manager):
            boss[man].append(k)

        def rec(k: int) -> int:
            if not boss[k]:
                return 0
            return informTime[k] + max(rec(x) for x in boss[k])
        
        return rec(headID)