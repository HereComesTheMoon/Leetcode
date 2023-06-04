class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        n = len(isConnected)
        res = 0
        for k in range(n):
            if k in seen:
                continue
            seen.add(k)
            now = { k }
            res += 1
            
            while now:
                i = now.pop()
                for j in range(n):
                    if isConnected[i][j] == 1 and j not in seen:
                        seen.add(j)
                        now.add(j)
        return res
