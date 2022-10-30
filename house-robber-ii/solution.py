class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        n = len(nums)
        nums = nums + nums
        maxi = 0
        for i in range(n):
            a, b = nums[i], nums[i]
            for k in range(2, n - 1):
                a, b = b, max(b, a + nums[i + k])
            maxi = max(maxi, b)
        
        return maxi
            
