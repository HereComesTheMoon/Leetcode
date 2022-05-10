class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for k in range(len(nums) - 2, -1, -1):
            if nums[k] < nums[k + 1]: 
                i = len(nums) - 1
                while nums[k] >= nums[i]:
                    i -= 1
                nums[k], nums[i] = nums[i], nums[k]

                for i in range(1, (len(nums) + 1 - k) // 2):
                    nums[k + i], nums[-i] = nums[-i], nums[k + i]
                return None
            
        nums.reverse()
        return None
