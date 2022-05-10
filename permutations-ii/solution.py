class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        result = []
        nums.sort()
        last = None
        for k, x in enumerate(nums):
            if x == last:
                continue
            result.extend([perm + [x] for perm in self.permuteUnique(nums[:k] + nums[k+1:])])
            last = x
        return result
