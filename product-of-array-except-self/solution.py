class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        cum = 1
        for i in range(len(nums)):
            res[i] *= cum
            cum *= nums[i]
        cum = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= cum
            cum *= nums[i]
        return res