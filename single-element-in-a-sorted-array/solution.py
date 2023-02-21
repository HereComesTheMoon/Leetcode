class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = 0
        b = len(nums) - 1
        while a < b:
            j = (b + a) // 2
            if nums[j] == nums[j+1]:
                pass
            elif nums[j] == nums[j-1]:
                j -= 1
            else:
                return nums[j]
            if (j - a) % 2:
                b = j - 1
            else:
                a = j + 2
        return nums[a]
