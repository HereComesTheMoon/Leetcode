class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        j = 1
        total = nums[0]

        # Find and Refine: Find a solution, then refine to find the best one
        while total < target and j < len(nums):
            total += nums[j]
            j += 1

        if total < target:
            return 0
        # Else: A solution exists.

        # Refine first solution
        while total >= target:
            total -= nums[i]
            i += 1

        length = j - i + 1

        # Move a shrinking window across the array, searching for solutions. When found, shrink window further
        while j < len(nums):
            total += nums[j]
            total -= nums[i]
            j += 1
            i += 1
            while total >= target:
                length -= 1
                total -= nums[i]
                i += 1

        return length
