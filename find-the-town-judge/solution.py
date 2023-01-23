class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        d_in = defaultdict(int)
        d_out: set[int] = set()
        for edge in trust:
            d_in[edge[1]] += 1
            d_out.add(edge[0])
        for k in range(1, n + 1):
            if d_in[k] < n - 1:
                continue
            if k in d_out:
                continue
            return k
        return -1
            