class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        data = [int(x) for x in matrix[0]]
        
        def largestRectangleInHistogram(heights: List[int]) -> int:
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

        largest = largestRectangleInHistogram(data)

        for row in matrix[1:]:
            for k, x in enumerate(row):
                if x == '0':
                    data[k] = 0
                else:
                    data[k] += 1
            
            largest = max(largest, largestRectangleInHistogram(data))
        return largest
