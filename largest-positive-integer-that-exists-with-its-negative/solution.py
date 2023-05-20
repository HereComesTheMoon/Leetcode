class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = set()
        res = -1
        for x in nums:
            if -x in d:
                res = max(res, abs(x))
            d.add(x)
        return res