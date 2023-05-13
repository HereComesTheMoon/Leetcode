class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        vals = [0 for _ in nums]
        now = 0
        for i in range(len(nums)):
            vals[i] = now
            now |= nums[i]
        now = 0
        for i in reversed(range(len(nums))):
            vals[i] |= now
            now |= nums[i]
        res = 0
        for x, others in zip(nums, vals):
            res = max(res, others | (x << k))
            
        return res
    