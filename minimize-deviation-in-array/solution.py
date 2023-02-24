import heapq as pq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        bound = float('-inf')
        for x in nums:
            if x % 2:
                heap.append((x, 2 * x))
                smallest = x
            else:
                smallest = x // (x & (~(x - 1)))
                heap.append((smallest, x))
            bound = max(bound, smallest)
        pq.heapify(heap)
        largest = bound
        min_dev = bound - heap[0][0]
        while heap:
            smallest, smallest_bound = heap[0]
            if smallest == smallest_bound:
                break
            if smallest == bound:
                break
            largest = max(largest, smallest * 2)
            pq.heapreplace(heap, (smallest * 2, smallest_bound))
            min_dev = min(min_dev, largest - heap[0][0])
        return min_dev