
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = { x : [] for x in range(n) }
        for start, goal, price in flights:
            d[start].append((goal, price))
        dists = [float("inf") for _ in range(n)]
        q = deque([
            (src, 0)
        ])

        while q and 0 <= k:
            for i in range(len(q)):
                pos, cost = q.popleft()
                for goal, price in d[pos]:
                    if dists[goal] <= cost + price:
                        continue
                    dists[goal] = cost + price
                    q.append((goal, cost + price))
            k -= 1

        if dists[dst] == float("inf"):
            return -1
        return dists[dst]