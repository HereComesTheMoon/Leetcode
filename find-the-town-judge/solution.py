class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        d_in: dict[int, int] = {}
        d_out: set[int] = set()
        for edge in trust:
            d_in[edge[1]] = d_in.get(edge[1], 0) + 1
            d_out.add(edge[0])
        for k, v in d_in.items():
            if v < n - 1:
                continue
            if k in d_out:
                continue
            return k
        return -1
            