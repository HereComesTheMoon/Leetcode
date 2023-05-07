# from collections import frozenset

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        chunks = [ [nums[0]] ]
        for x in nums[1:]:
            if x == chunks[-1][0]:
                chunks[-1].append(x)
            else:
                chunks.append([x])
        
        res = [[]]
        for chunk in chunks:
            now = [ subset + [ chunk[0] ] for subset in res ]
            res.extend(now)
            for k in range(1, len(chunk)):
                now = [ subset + [ chunk[0] ] for subset in now ]
                res.extend(now)
        return res