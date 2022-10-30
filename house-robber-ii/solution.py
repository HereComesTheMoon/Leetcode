class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        a, b = nums[0], max(nums[0], nums[1])
        c, d = nums[1], max(nums[1], nums[2])
        for k in range(2, len(nums) - 1):
            a, b = b, max(b, a + nums[k])
            c, d = d, max(d, c + nums[k + 1])
        
        return max(b, d)
