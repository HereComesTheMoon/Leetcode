class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = { x : [] for x in range(n) }
        shortest = -1
        found = False
        for start, goal, price in flights:
            shortest = max(shortest, price)
            d[start].append((goal, price))
        
        new_reachable = { src }
        reachable = { src }
        while new_reachable:
            now = new_reachable.pop()
            for goal, _ in d[now]:
                if goal not in reachable:
                    new_reachable.add(goal)
                    reachable.add(goal)
        if dst not in reachable:
            return -1
        


        shortest = shortest * (k + 2)

        stack = [
            (0, src, -1)
        ]

        while stack:
            price, pos, num_stops = stack.pop()
            if pos == dst:
                shortest = min(shortest, price)
                found = True
            if num_stops == k:
                continue
            for goal, cost in d[pos]:
                if shortest < price + cost:
                    continue
                stack.append((price + cost, goal, num_stops + 1))
        
        if found:
            return shortest
        else:
            return -1
