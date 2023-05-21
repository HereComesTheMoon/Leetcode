class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 1
            else:
                return 0

        a = 0
        b = len(nums)
        while a < b:
            mid = (a + b) // 2
            if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                a = mid + 1
            else:
                b = mid
        return a