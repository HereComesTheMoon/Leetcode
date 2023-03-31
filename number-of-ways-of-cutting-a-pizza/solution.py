class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        xx = len(pizza[0])
        yy = len(pizza)

        apples = [[0 for _ in range(xx + 1)] for _ in range(yy + 1)]
        for row in range(yy - 1, -1, -1):
            for col in range(xx - 1, -1, -1):
                apples[row][col] = ((pizza[row][col] == 'A')
                                    + apples[row + 1][col]
                                    + apples[row][col + 1]
                                    - apples[row + 1][col + 1])
        dp = [[int(apples[y][x] > 0) for x in range(xx)] for y in range(yy)]        
        MOD = 1_000_000_007
        for _ in range(1, k):
            new = [[0 for _ in row] for row in pizza]
            for y in range(yy):
                for x in range(xx):
                    for vert in range(y + 1, yy):
                        if apples[y][x] > apples[vert][x]:
                            new[y][x] += dp[vert][x]
                    for horz in range(x + 1, xx):
                        if apples[y][x] > apples[y][horz]:
                            new[y][x] += dp[y][horz]
                    new[y][x] %= MOD
            dp = new
        return dp[0][0]

