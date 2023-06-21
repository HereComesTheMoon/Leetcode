class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums = list(sorted( (x,y) for x, y in zip(nums, cost)))

        @functools.cache
        def cost(target: int) -> int:
            return sum(abs(target - x) * y for x, y in nums)
            
        a = nums[0][0]
        b = nums[-1][0]
        while a + 2 < b:
            third = (b - a) // 3
            c = a + third
            d = b - third
            if cost(c) <= cost(d):
                b = d
            else:
                a = c
        return min(cost(x) for x in range(a, a + 3))   


