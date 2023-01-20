class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        k = 0
        while k < len(nums):
            first = nums[k]
            last = nums[k]
            k += 1
            while k < len(nums) and nums[k] == last + 1:
                k += 1
                last += 1
            if first == last:
                res.append(f"{first}")
            else:
                res.append(f"{first}->{last}")
        return res
