class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        edges = [ set() for _ in range(len(roads) + 1) ]
        for a, b in roads:
            edges[a].add(b)
            edges[b].add(a)
                
        def rec(vertex: int) -> Tuple[int, int]:
            if not edges[vertex]:
                return (1, 1)
            
            fuel = 0
            people = 1
            for goal in edges[vertex]:
                edges[goal].discard(vertex)
                more_fuel, more_people = rec(goal)
                fuel += more_fuel
                people += more_people
            
            fuel += 1 + ((people - 1) // seats)
            return fuel, people
        
        total_fuel = 0
        for vertex in edges[0]:
            edges[vertex].discard(0)
            fuel, _ = rec(vertex)
            total_fuel += fuel
        return total_fuel

