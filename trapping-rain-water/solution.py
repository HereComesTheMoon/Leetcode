class Solution:
    def trap(self, heights: list[int]) -> int:
        front, back = 0, len(heights) - 1
        front_peak, back_peak = heights[front], heights[back]
        total = 0
        while front < back:
            if heights[front] <= heights[back]:
                if heights[front] < front_peak:
                    total += front_peak - heights[front]
                else:
                    front_peak = heights[front]
                front += 1
            else:
                if heights[back] < back_peak:
                    total += back_peak - heights[back]
                else:
                    back_peak = heights[back]
                back -= 1

        return total
