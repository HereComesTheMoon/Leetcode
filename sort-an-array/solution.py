class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        n = len(nums) // 2
        l = self.sortArray(nums[:n])
        r = self.sortArray(nums[n:])
        i = 0
        j = 0
        res = [0] * len(nums)
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                res[i+j] = l[i]
                i += 1
            else:
                res[i+j] = r[j]
                j += 1
        while i < len(l):
            res[i+j] = l[i]
            i += 1
        while j < len(r):
            res[i+j] = r[j]
            j += 1
        return res
