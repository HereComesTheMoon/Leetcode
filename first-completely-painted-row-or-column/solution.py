class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        table = {
            mat[i][j] : (i, j) for i in range(m) for j in range(n)
        }
        assert len(table) == n * m
        rows = { k: 0 for k in range(m) }
        cols = { k: 0 for k in range(n) }
        for k, x in enumerate(arr):
            i, j = table[x]
            rows[i] += 1
            if rows[i] == n:
                return k
            cols[j] += 1
            if cols[j] == m:
                return k
        assert False
            