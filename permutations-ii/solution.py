class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        result = []
        for k, x in enumerate(nums):
            result.extend([perm + [x] for perm in self.permuteUnique(nums[:k] + nums[k+1:])])

        result = list(set( tuple(x) for x in result ))
        return [list(x) for x in result]
