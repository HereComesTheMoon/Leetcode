class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        total = total // 2
        sums = { 0 }
        for x in nums:
            if total in sums:
                return True
            sums |= { x + y for y in sums }
        return total in sums
