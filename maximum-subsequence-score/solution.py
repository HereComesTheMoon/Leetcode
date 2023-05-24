import heapq as pq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [ (y, x) for x, y in zip(nums1, nums2) ]
        nums.sort(reverse=True)

        now = [ row[1] for row in nums[:k] ]
        pq.heapify(now)
        summed = sum(now)
        res = summed * nums[k-1][0]
        for [mini, plus] in nums[k:]:
            lost = pq.heapreplace(now, plus)
            summed -= lost
            summed += plus
            res = max(res, mini * summed)
        return res
            

