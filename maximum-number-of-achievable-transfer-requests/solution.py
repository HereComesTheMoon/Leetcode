class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        def rec(trfs: List[int], pos: int) -> int:
            if len(requests) - pos < sum(map(abs, trfs)) // 2:
                return -999999
            if pos == len(requests):
                return 0
            if requests[pos][0] == requests[pos][1]:
                return 1 + rec(trfs, pos + 1)
            res = rec(trfs, pos + 1)
            [tail, head] = requests[pos]
            trfs[tail] -= 1
            trfs[head] += 1
            res = max(res, 1 + rec(trfs, pos + 1))
            trfs[tail] += 1
            trfs[head] -= 1
            return res
        
        return rec([0] * n, 0)
