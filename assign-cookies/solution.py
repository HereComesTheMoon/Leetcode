class Solution:
    def findContentChildren(self, greed: List[int], size: List[int]) -> int:
        greed.sort()
        size.sort()
        i = 0
        res = 0
        for s in size:
            if i == len(greed):
                break
            if greed[i] <= s:
                i += 1
                res += 1
        return res
