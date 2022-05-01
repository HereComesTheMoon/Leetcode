class Solution:
    def trap(self, heights: list[int]) -> int:
        maxi = int(max(range(len(heights)), key=heights.__getitem__))
        peak, nxt = 0, 1
        rocks = 0
        total = 0

        while nxt <= maxi:
            if heights[nxt] < heights[peak]:
                rocks += heights[nxt]
            else:
                total += (nxt - peak - 1) * heights[peak] - rocks
                rocks = 0
                peak = nxt
            nxt += 1

        peak, nxt = len(heights) - 1, len(heights) - 2
        rocks = 0

        while maxi <= nxt:
            if heights[nxt] < heights[peak]:
                rocks += heights[nxt]
            else:
                total += (peak - nxt - 1) * heights[peak] - rocks
                rocks = 0
                peak = nxt
            nxt -= 1
        return total

