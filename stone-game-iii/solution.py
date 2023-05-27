class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total = sum(stoneValue)
        
        @functools.cache
        def rec(i: int, turn: bool) -> int:
            if len(stoneValue) <= i:
                return 0
            if turn:
                return max(
                    sum(stoneValue[i:j]) + rec(j, False) for j in range(i + 1, i + 4)
                )
            else:
                return min(
                    rec(j, True) for j in range(i + 1, i + 4)
                )
        
        res = rec(0, True)
        if res * 2 == total:
            return "Tie"
        if res * 2 < total:
            return "Bob"
        return "Alice"

