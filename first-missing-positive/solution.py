class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for k in range(n):
            if nums[k] <= 0 or n < nums[k]:
                nums[k] = n + 1
        
        for x in nums:
            x = abs(x)
            if x == n + 1:
                continue
            nums[x-1] = - abs(nums[x-1])

        for k in range(n):
            if 0 < nums[k]:
                return k + 1
        return n + 1