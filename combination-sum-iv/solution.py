from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums.sort()

        @cache
        def count(target: int) -> int:
            if target <= 0:
                return 1 if target == 0 else 0
            
            return sum( count(target - x) for x in nums)

        return count(target)