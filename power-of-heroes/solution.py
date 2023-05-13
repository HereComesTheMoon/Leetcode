class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        MOD = 1_000_000_007
        power = 0
        dp = [None for _ in nums]
        dp[-1] = nums[-1]**2
        for k in reversed(range(len(nums) - 1)):
            dp[k] = ((dp[k+1] * 2) + nums[k]**2) % MOD
            
        a = [None for _ in nums]
        a[-1] = dp[-1]
        for k in range(len(dp) - 1):
            a[k] = dp[k+1] + nums[k]**2
            
        for i in range(len(nums)):
            power += nums[i] * a[i]
                
        return power % MOD