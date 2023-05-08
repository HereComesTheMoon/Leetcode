class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for k in range(n):
            res += mat[k][k]
            res += mat[k][n-1-k]
        if n % 2 == 1:
            res -= mat[n // 2][n // 2]
        return res