class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    
        skillGraph = defaultdict(set)
        N = len(req_skills)
        for ind, p in enumerate(people):
            for skill in p:
                skillGraph[skill].add(ind)
        
        ans = list(range(N+1))
        
        def DFS(peopleSet, k):
            nonlocal ans
            if k == N:
                if len(ans) > len(peopleSet):
                    ans = list(peopleSet)
                return 
            if len(peopleSet) >= len(ans):
                return 
            for p in peopleSet:
                if p in skillGraph[req_skills[k]]:
                    DFS(peopleSet, k+1)
                    return 
            for p in skillGraph[req_skills[k]]:
                peopleSet.add(p)
                DFS(peopleSet, k+1)
                peopleSet.remove(p)
        
        DFS(set(), 0)
        
        return ans