class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        while a < b:
            mid = (a + b) // 2
            if nums[mid] < target:
                a = mid + 1
            else:
                b = mid
        return a if nums[a] == target else -1
