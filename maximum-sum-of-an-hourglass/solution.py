class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def hourglass(i, j) -> int:
            return sum(grid[i+ii][j+jj] for ii, jj in [
                (0,0), (0,1), (0,2),
                       (1,1),
                (2,0), (2,1), (2,2),
            ])
        
        return max(hourglass(i, j) for i in range(len(grid)-2) for j in range(len(grid[0])-2))