class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for x, count in c.most_common():
            if count == 1:
                return x