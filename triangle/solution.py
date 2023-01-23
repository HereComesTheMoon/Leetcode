class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cost = [0 for _ in triangle[-1]]
        cost[0] = triangle[0][0]
        for y in range(1, len(triangle)):
            temp = cost[0]
            cost[0] = temp + triangle[y][0]
            for x in range(1, len(triangle[y]) - 1):
                new_val = triangle[y][x] + min(temp, cost[x])
                temp = cost[x]
                cost[x] = new_val
            cost[len(triangle[y]) - 1] = temp + triangle[y][-1]
        return min(cost)