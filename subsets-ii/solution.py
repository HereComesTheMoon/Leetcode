class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        vals = []
        last = nums[0] - 1
        for x in nums:
            if x == last:
                vals[-1].append(x)
            else:
                vals.append([x])
            last = x

        res = [[]]
        for row in vals:
            new_sets = deepcopy(res)
            for x in row:
                for subset in new_sets:
                    subset.append(x)
                res.extend(deepcopy(new_sets))
                                       
        return res