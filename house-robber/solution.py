class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        a = nums[0]
        b = max(nums[0], nums[1])
        for x in nums[2:]:
            c = max(a + x, b)
            a = b
            b = c
        return b