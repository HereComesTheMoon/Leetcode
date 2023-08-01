class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if n % 2 == 1:
            return False
        n = n // 2

        @functools.cache
        def rec(val: int, pos: int) -> int:
            if n <= val:
                return val == n
            if pos == len(nums):
                return False
            return rec(val, pos + 1) or rec(val + nums[pos], pos + 1)
        
        return rec(0, 0)

