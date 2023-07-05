class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not (0 in nums):
            return len(nums) - 1
        res = [0,0]
        for x in nums:
            if x == 1:
                res[-1] += 1
            elif res[-1] != 0 or res[-2] != 0:
                res.append(0)
        return max(x + y for x, y in zip(res, res[1:]))