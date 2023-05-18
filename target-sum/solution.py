from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort(reverse=True)

        @cache
        def rec(i: int, val: int) -> int:
            if i == len(nums):
                return 1 if val == target else 0
            return rec(i + 1, val + nums[i]) + rec(i + 1, val - nums[i])

        return rec(0, 0)
