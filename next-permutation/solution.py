
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 2
        while k >= 0:
            if nums[k] < nums[k + 1]:
                i = k + 1 + self.binSearch(nums[k+1:], nums[k])
                nums[k], nums[i] = nums[i], nums[k]
                nums[k+1:] = reversed(nums[k+1:])
                return None
            k -= 1

        nums.reverse()
        return None

    def binSearch(self, nums: list[int], goal: int) -> int:
        """Search in descending sorted list nums[l:r] until you find element > goal. Return index ."""
        if len(nums) == 1 or nums[-1] > goal:
            return len(nums) - 1

        j = len(nums) // 2
        k = j

        while k >= 1:
            k = k // 2
            if nums[j] <= goal:
                j -= k
            elif nums[j+1] >= goal:
                j += k

        while nums[j] <= goal:
            j -= 1
        while nums[j+1] > goal:
            j += 1

        return j
