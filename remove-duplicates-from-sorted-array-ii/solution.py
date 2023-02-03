class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 2
        i = 1
        j = 2
        while j < len(nums):
            if nums[i] < nums[j] or nums[i-1] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
            
        return i + 1


        