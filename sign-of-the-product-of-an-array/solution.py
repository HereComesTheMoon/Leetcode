class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = True
        for x in nums:
            if x == 0:
                return 0
            sign ^= x < 0
        return 1 if sign else -1