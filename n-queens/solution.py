from itertools import permutations


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]
        if n == 2 or n == 3:
            return []
        
        def check(cand) -> bool:
            cand = list(enumerate(cand))
            for a, b in cand:
                for p, q in cand[a+1:]:
                    if p + b == q + a or p + q == b + a:
                        return False
            return True
                        
            
        solutions = []
        
        for cand in permutations(range(n)):
            if check(cand):
                solutions.append([ "."*y + "Q" + "."*(n-y-1) for y in cand ])
        
        return solutions
                
            
            
        