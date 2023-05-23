import heapq as pq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = list(sorted(nums, reverse=True))[:k]
        pq.heapify(self.nums)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            pq.heappush(self.nums, val)
            return self.nums[0]
        if val <= self.nums[0]:
            return self.nums[0]
        pq.heapreplace(self.nums, val)
        return self.nums[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)