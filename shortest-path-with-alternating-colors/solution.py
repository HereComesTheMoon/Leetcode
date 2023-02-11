from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        resr = [None for _ in range(n)]
        resb = [None for _ in range(n)]
        resr[0] = 0
        resb[0] = 0
        reds = [ set() for _ in range(n) ]
        blues = [ set() for _ in range(n) ]

        for tail, head in redEdges:
            reds[tail].add(head)
        
        for tail, head in blueEdges:
            blues[tail].add(head)

        qr = deque(reds[0])
        qb = deque(blues[0])

        level = 1
        while qr or qb:
            cycler = len(qr)
            cycleb = len(qb)
            for _ in range(cycler):
                now = qr.popleft()
                if resr[now] is not None:
                    continue
                resr[now] = level
                for adj in blues[now]:
                    qb.append(adj)

            for _ in range(cycleb):
                now = qb.popleft()
                if resb[now] is not None:
                    continue
                resb[now] = level
                for adj in reds[now]:
                    qr.append(adj)
            
            level += 1

        for k in range(n):
            match (resr[k], resb[k]):
                case (None, None):
                    resr[k] = -1
                case (_, None):
                    pass
                case (None, _):
                    resr[k] = resb[k]
                case _:
                    resr[k] = min(resr[k], resb[k])
        return resr

        

