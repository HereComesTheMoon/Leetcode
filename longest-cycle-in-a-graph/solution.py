class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        seen = [0 for _ in range(n)]
        longest = -1
        def cycle(x: int) -> int:
            if seen[x] != 0:
                return -1
            root = x
            i = 0
            while seen[x] == 0:
                seen[x] = i
                i += 1
                x = edges[x]
                if x == -1 or seen[x] == -1:
                    y = root
                    for _ in range(i):
                        seen[y] = -1
                        nxt = edges[y]
                        edges[y] = -1
                        y = nxt
                    return -1
            result = i - seen[x]
            y = root
            for _ in range(i- 2):
                seen[y] = -1
                nxt = edges[y]
                edges[y] = -1
                y = nxt
            return result
        for x in range(n):
            longest = max(longest, cycle(x))
        return longest
