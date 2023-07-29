class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()

        @functools.cache
        def rec(start: int) -> int:
            if start == len(nums):
                return 0
            val = nums[start]
            i = start
            while i < len(nums) and nums[i] == val:
                i += 1
            if i == len(nums) or nums[i] != val + 1:
                return (i - start) * val + rec(i)
            else:
                j = i
                while j < len(nums) and nums[j] == val + 1:
                    j += 1
                return max(rec(i), (i - start) * val + rec(j))
        
        return rec(0)
