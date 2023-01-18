class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]
        for x in nums:
            counter[x] += 1
        for k in range(counter[0]):
            nums[k] = 0
        for k in range(counter[0], counter[0] + counter[1]):
            nums[k] = 1
        for k in range(counter[0] + counter[1], len(nums)):
            nums[k] = 2
