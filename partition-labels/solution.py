class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for k, x in enumerate(s):
            last[x] = k
        res = [0]
        for k, x in enumerate(s):
            if res[-1] < k:
                res.append(last[x])
            else:
                res[-1] = max(res[-1], last[x])
        partial = -1
        for k, val in enumerate(res):
            res[k] -= partial
            partial = val
        return res