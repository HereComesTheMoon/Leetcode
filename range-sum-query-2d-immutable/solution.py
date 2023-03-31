class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[None for _ in row] for row in matrix]
        xx = len(matrix[0]) - 1 
        yy = len(matrix) - 1
        self.xx = xx
        self.yy = yy
        cum = 0
        # self.dp[-1][-1] = matrix[-1][-1]
        for x in range(xx + 1):
            cum += matrix[yy][xx-x]
            self.dp[yy][xx-x] = cum

        cum = 0
        for y in range(yy + 1):
            cum += matrix[yy-y][xx]
            self.dp[yy-y][xx] = cum

        for y in range(1, yy + 1):
            for x in range(1, xx + 1):
                self.dp[yy-y][xx-x] = matrix[yy-y][xx-x] + self.dp[yy-y+1][xx-x] + self.dp[yy-y][xx-x+1] - self.dp[yy-y+1][xx-x+1]
        print(self.dp)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.dp[row1][col1]
        if row2 < self.yy:
            res -= self.dp[row2+1][col1]
        if col2 < self.xx:
            res -= self.dp[row1][col2+1]
        if row2 < self.yy and col2 < self.xx:
            res += self.dp[row2+1][col2+1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)