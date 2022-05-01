import heapq

class Solution:
    def trap(self, height_list: list[int]) -> int:
        total = 0
        pq = [(-height, index, total := total + height) for index, height in enumerate(height_list)]
        heapq.heapify(pq)

        first = heapq.heappop(pq)
        left, right = first, first
        total = 0

        while pq:
            nxt = heapq.heappop(pq)
            if nxt[1] < left[1]:
                total += (1 + nxt[1] - left[1]) * max(left[0], nxt[0]) - left[2] + nxt[2] - left[0]
                left = nxt
            if right[1] < nxt[1]:
                total += (right[1] + 1 - nxt[1]) * max(right[0], nxt[0]) - nxt[2] + right[2] - nxt[0]
                right = nxt

        return total