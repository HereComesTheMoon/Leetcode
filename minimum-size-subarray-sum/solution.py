class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        val = 0
        res = len(nums) + 1
        while j < len(nums):
            if val < target:
                val += nums[j]
                j += 1
            else:
                res = min(res, j - i)
                val -= nums[i]
                i += 1
        if target <= val:
            while target <= val - nums[i]:
                val -= nums[i]
                i += 1
            res = min(res, j - i)
        
        return res if res <= len(nums) else 0