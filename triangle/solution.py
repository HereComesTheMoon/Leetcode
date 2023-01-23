class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cost = [
            [0 for _ in row] for row in triangle
        ]
        cost[0][0] = triangle[0][0]
        for y in range(1, len(triangle)):
            cost[y][0] = cost[y-1][0] + triangle[y][0]
            for x in range(1, len(triangle[y]) - 1):
                cost[y][x] = triangle[y][x] + min(cost[y-1][x-1], cost[y-1][x])
            cost[y][-1] = cost[y-1][-1] + triangle[y][-1]
        return min(cost[-1])