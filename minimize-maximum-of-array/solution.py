class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        total = nums[0]
        for k, x in enumerate(nums[1:], 2):
            total += x
            res = max(res, math.ceil(total / k))
        return res
