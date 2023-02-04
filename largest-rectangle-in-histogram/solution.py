class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        largest = 0
        stack = [ (0, heights[0]) ]
        for i in range(1, len(heights)):
            if heights[i - 1] < heights[i]:
                stack.append( (i, heights[i]) )
                continue
            if heights[i - 1] == heights[i]:
                continue
            earliest = i
            while stack and heights[i] < stack[-1][1]:
                start, height = stack.pop()
                earliest = min(start, earliest)
                largest = max(largest, (i - start) * height)
            stack.append( (earliest, heights[i]) )
        
        while stack:
            start, height = stack.pop()
            largest = max(largest, (len(heights) - start) * height)
 

        return largest
