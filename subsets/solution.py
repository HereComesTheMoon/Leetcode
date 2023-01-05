class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        rec = self.subsets(nums[1:])
        return rec + [ subset + [nums[0]] for subset in rec ]