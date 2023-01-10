class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while True:
            mid = (j + i) // 2
            val = nums[mid]
            if val == target:
                return mid
            if mid == i:
                return -1
            if target < val:
                j = mid
            else:
                i = mid