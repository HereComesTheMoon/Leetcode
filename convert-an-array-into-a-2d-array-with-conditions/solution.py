from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        num_rows = c.most_common(1)[0][1]
        res = [ [] for _ in range(num_rows) ]
        for x, count in c.items():
            for k in range(count):
                res[k].append(x)
        return res