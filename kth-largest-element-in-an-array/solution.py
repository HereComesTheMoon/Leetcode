import heapq as pq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        pq.heapify(heap)
        for x in nums[k:]:
            if x <= heap[0]:
                continue
            pq.heapreplace(heap, x)
        return heap[0]