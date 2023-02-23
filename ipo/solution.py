import heapq as pq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = list(project for project in zip(capital, profits))
        projects.sort()
        i = 0
        while i < len(projects) and projects[i][0] <= w:
            pq.heappush(heap, -projects[i][1])
            i += 1

        for _ in range(k):
            if not heap:
                break
            w += - pq.heappop(heap)
            while i < len(projects) and projects[i][0] <= w:
                pq.heappush(heap, -projects[i][1])
                i += 1
        
        return w
    