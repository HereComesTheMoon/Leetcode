class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        result = []

        for k, x in enumerate(nums):
            result.extend(perm + [x] for perm in self.permute(nums[:k] + nums[k+1:]))

        return result
