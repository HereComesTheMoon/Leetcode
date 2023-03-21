class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        run = 0
        for x in nums:
            if x != 0:
                count += (run * (run + 1)) // 2
                run = 0
            else:
                run += 1
        count += (run * (run + 1)) // 2
        return count