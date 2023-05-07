from bisect import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        vals = []
        for k, height in enumerate(nums):
            idx = bisect(vals, height)
            if idx == len(vals):
                vals.append(height)
            else:
                vals[idx] = height
            res[k] = idx + 1
        return res

