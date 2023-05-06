from bisect import bisect

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        i = 0
        MOD = 1_000_000_007
        while i < len(nums) and nums[i] <= (target + 1) // 2:
            j = bisect(nums, target - nums[i], i)
            res += pow(2, j - i) // 2
            i += 1
        return res % MOD



