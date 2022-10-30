class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        A = [nums[0], max(nums[0], nums[1])] + [None]*(len(nums) - 2)
        for k in range(2, len(nums)):
            A[k] = max(A[k-1], A[k-2] + nums[k])
        return A[-1]
        
        