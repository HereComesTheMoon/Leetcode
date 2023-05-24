class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        res = 0
        for x in nums:
            if x == 1:
                c += 1
            else:
                c = 0
            res = max(res, c)
        return res