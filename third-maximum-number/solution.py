import heapq as pq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res = []
        for x in nums:
            if x in res:
                continue
            if len(res) < 3:
                res.append(x)
                continue
            if res and x < min(res):
                continue
            res.append(x)
            if 3 < len(res):
                res.sort(reverse=True)
                res.pop()
        if len(res) == 3:
            return min(res)
        else:
            return max(res)        