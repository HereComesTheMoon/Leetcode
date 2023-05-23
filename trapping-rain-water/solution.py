class Solution:
    def trap(self, height: List[int]) -> int:
        peaksl = [ 0 for _ in height ]
        maxl = height[0]
        for k in range(len(height)):
            peaksl[k] = maxl
            maxl = max(maxl, height[k])

        peaksr = [ 0 for _ in height ]
        maxr = height[-1]
        for k in reversed(range(len(height))):
            peaksr[k] = maxr
            maxr = max(maxr, height[k])
        
        res = 0
        for k, x in enumerate(height):
            res += max(min(peaksl[k], peaksr[k]) - x, 0)
        
        return res