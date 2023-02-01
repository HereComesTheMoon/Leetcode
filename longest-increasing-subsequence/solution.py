from bisect import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        res = [nums[0]]
        for x in nums[1:]:
            pos = bisect(res, x)
            if pos == 0:
                res[0] = x
                continue
            if res[pos - 1] == x:
                continue
            if pos == len(res):
                res.append(x)
                continue
            res[pos] = x
        return len(res)






[5,6,7,1,2,3,4]