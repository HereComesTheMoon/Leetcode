class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        loc1 = len(nums) // 2
        loc2 = (len(nums) - 1) // 2
        return (nums[loc1] + nums[loc2]) / 2
