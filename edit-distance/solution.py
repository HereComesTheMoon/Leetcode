class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1
        dp = [ [ None for _ in range(m) ] for _ in range(n) ]
        for j in range(m):
            dp[0][j] = j
        
        for i in range(1, n):
            dp[i][0] = i
            for j in range(1, m):
                dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j - 1], dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))
            
        return dp[-1][-1]
