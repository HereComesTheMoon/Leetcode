from copy import deepcopy

class DSU:
    def __init__(self, n: int):
        self.d = list(range(n))
        self.weights = [1] * n
    
    def get(self, x: int) -> int:
        while self.d[x] != x:
            self.d[x] = self.d[self.d[x]]
            x = self.d[x]
        return x

    def merge(self, a: int, b: int):
        a = self.get(a)
        b = self.get(b)
        if self.weights[a] < self.weights[b]:
            self.d[a] = b
            self.weights[b] += self.weights[a]
        else:
            self.d[b] = a
            self.weights[a] += self.weights[b]
        

class Solution:
    def maxNumEdgesToRemove(self, n: int, edge_list: List[List[int]]) -> int:
        edges = [ [], [], [] ]
        for [typ, a, b] in edge_list:
            edges[typ - 1].append((a-1, b-1))
        
        dsu = DSU(n)
        result = 0
        for [a, b] in edges[2]:
            if dsu.get(a) != dsu.get(b):
                dsu.merge(a, b)
            else:
                result += 1
        
        dsua = deepcopy(dsu)
        for [a, b] in edges[0]:
            if dsua.get(a) != dsua.get(b):
                dsua.merge(a, b)
            else:
                result += 1

        for [a, b] in edges[1]:
            if dsu.get(a) != dsu.get(b):
                dsu.merge(a, b)
            else:
                result += 1
        
        aa = { dsua.get(k) for k in range(n) }
        bb = {  dsu.get(k) for k in range(n) }
        if aa != bb or len(aa) != 1:
            return -1
        
        return result







        



