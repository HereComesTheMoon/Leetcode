class DSU:
    def __init__(self, n: int):
        self.d = list(range(n))
        self.weights = [0] * n
        
    def get(self, a: int) -> int:
        while a != self.d[a]:
            self.d[a] = self.d[self.d[a]]
            a = self.d[a]
        return a
    
    def merge(self, a: int, b: int) -> int:
        a = self.get(a)
        b = self.get(b)
        if self.weights[a] < self.weights[b]:
            self.weights[b] += self.weights[a]
            self.d[a] = b
        else:
            self.weights[a] += self.weights[b]
            self.d[b] = a

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for [a, b] in edges:
            dsu.merge(a, b)
        nodes = { dsu.get(a) : 0 for a in range(n) }
        for a in range(n):
            nodes[dsu.get(a)] += 1
            
        edgecount = { dsu.get(a) : 0 for a in range(n) } 
        for [a, b] in edges:
            edgecount[dsu.get(a)] += 1
            
        res = 0
        for comp, num_nodes in nodes.items():
            if edgecount[dsu.get(comp)] * 2 == num_nodes * (num_nodes - 1):
                res += 1
        return res
            