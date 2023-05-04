from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        numr = sum(x == 'R' for x in senate)
        numd = len(senate) - numr
        delr = 0
        deld = 0
        q = deque(senate)
        while q:
            if numr == 0:
                return "Dire"
            if numd == 0:
                return "Radiant"
            nxt = q.popleft()
            print(nxt)
            if nxt == "R":
                if 0 < delr:
                    delr -= 1
                    continue
                deld += 1
                numd -= 1
                q.append("R")
            else:
                if 0 < deld:
                    deld -= 1
                    continue
                delr += 1
                numr -= 1
                q.append("D")
        assert False