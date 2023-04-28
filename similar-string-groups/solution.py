class UnionFind:
    def __init__(self, vals: List[str]):
        self.d = {
            val: val for val in vals
        }
        self.weight = {
            val: 1 for val in vals
        }

    def get(self, w: str) -> str:
        par = w
        w = self.d[w]
        while par != w:
            new_par = w
            w = self.d[w]
            self.d[par] = w
            par = new_par
        return w
        

    def merge(self, a: str, b: str) -> str:
        a = self.get(a)
        b = self.get(b)
        if self.weight[a] < self.weight[b]:
            self.d[a] = b
            self.weight[a] += self.weight[b]
            return b
        else:
            self.d[b] = a
            self.weight[b] += self.weight[a]
            return a
        


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind(strs)
        for k, a in enumerate(strs):
            for b in strs[k:]:
                if uf.get(a) == uf.get(b):
                    continue
                if sum(1 if ca != cb else 0 for ca, cb in zip(a, b)) == 2:
                    uf.merge(a, b)
        return len({uf.get(w) for w in strs})