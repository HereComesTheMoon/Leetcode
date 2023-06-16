class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(nums):
            m = len(nums)
            if m < 3: 
                return 1
            left = []
            right = []
            for a in nums:
                if a < nums[0]:
                    left.append(a)
                elif nums[0] < a:
                    right.append(a)
            return dfs(left) * dfs(right) * comb(m - 1, len(left)) % mod
        
        return (dfs(nums) - 1) % mod