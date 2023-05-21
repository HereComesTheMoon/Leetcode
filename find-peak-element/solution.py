class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a = 0
        b = len(nums)
        while a < b:
            mid = (a + b) // 2
            if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                a = mid + 1
            else:
                b = mid
        return a