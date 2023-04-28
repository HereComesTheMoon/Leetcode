# Testin other solution to see if it is faster than mine 
class DSU:
    def __init__(self, l):
        self.memo = [i for i in range(l)]
    
    def find(self, x):
        if self.memo[x] != x:
            self.memo[x] = self.find(self.memo[x])
        return self.memo[x]

    def union(self, x, y):
        x_r = self.find(x)
        y_r = self.find(y)

        if x_r != y_r:
            self.memo[x_r] = y_r




class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def helper(s1, s2):
            if s1 == s2:
                return True
            ct = 0
            for i, j in zip(s1, s2):
                if i != j:
                    if ct == 2:
                        return False
                    ct += 1
            
            return True
        
        dsu = DSU(len(strs))
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if helper(strs[i], strs[j]):
                    dsu.union(i, j)
        
        return len(set([dsu.find(i) for i in range(len(strs))]))