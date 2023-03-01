class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        res = []
        while nums:
            res.append(heappop(nums))
        return res