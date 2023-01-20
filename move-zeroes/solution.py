class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for x in nums:
            if x == 0:
                continue
            nums[i] = x
            i += 1
        for k in range(i, len(nums)):
            nums[k] = 0
