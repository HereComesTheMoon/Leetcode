class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k, x in enumerate(nums):
            if x in d:
                return [d[x], k]
            d[target - x] = k
        