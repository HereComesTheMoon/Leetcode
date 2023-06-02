class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        close = { k: set() for k in range(len(bombs)) }
        def p_reaches_q(p, q) -> bool:
            return (q[0] - p[0])**2 + (q[1] - p[1])**2 <= p[2]**2
        for i, p in enumerate(bombs):
            for j, q in enumerate(bombs):
                if p_reaches_q(p, q):
                    close[i].add(j)
            close[i].discard(i)
        
        def rec(k: int):
            res = 1
            for i in close[k]:
                if i in seen:
                    continue
                seen.add(i)
                res += rec(i)
            return res
            
        res = 0
        for k in range(len(bombs)):
            seen = {k}
            res = max(res, rec(k))
        return res