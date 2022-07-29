class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for k, v in enumerate(nums):
            b = d.get(target - v, None)
            if b is not None:
                return [k, b]
            d[v] = k
