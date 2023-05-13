class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        score = 0
        while nums[0]:
            score += max(row.pop() for row in nums)
        return score