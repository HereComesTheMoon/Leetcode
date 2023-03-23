class DisjointSet:
    def __init__(self, n: int):
        self.v = list(range(n))
        self.w = [1 for _ in range(n)]
    
    def get(self, n: int) -> int:
        last = n
        n = self.v[n]
        while last != n:
            temp = self.v[n]
            self.v[last] = temp
            last = n
            n = temp
        return n
    
    def merge(self, a: int, b: int) -> bool:
        a = self.get(a)
        b = self.get(b)
        if a == b:
            return True
        if self.w[a] < self.w[b]:
            a, b = b, a
        self.v[b] = a
        self.w[a] += self.w[b]
        return False



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        free_cables = 0
        for [a, b] in connections:
            free_cables += 1 if ds.merge(a, b) else 0
        num_comp = len({ds.get(x) for x in range(n)})
        if free_cables < num_comp - 1:
            return -1
        return num_comp - 1



