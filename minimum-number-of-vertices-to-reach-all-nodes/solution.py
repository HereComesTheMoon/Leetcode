class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(range(n))
        for [a, b] in edges:
            res.discard(b)
        return list(res)

        # ein = { k : [] for k in range(n) }
        # eout = { k : 0 for k in range(n) }
        # for [a, b] in edges:
        #     ein[b].append(a)
        #     eout[a] += 1
        # leaves = { k for k, v in eout.items() if v == 0 }
        # res = { k for k in range(n) }
        # while leaves:
        #     now = leaves.pop()
        #     res.discard(now)
        #     for k in ein[now]:
        #         eout[k] -= 1
        #         if eout[k] == 0:
        #             leaves.add(k)
                
        # return list(res)
