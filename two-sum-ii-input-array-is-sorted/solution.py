from bisect import bisect_right, bisect_left
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while True:
            if nums[i] + nums[j] < target:
                i = bisect_left(nums, target - nums[j], i, j)
            elif nums[i] + nums[j] > target:
                j = bisect_right(nums, target - nums[i], i, j) - 1
            else:
                break
        return [i + 1, j + 1]
