from itertools import permutations


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]
        if n == 2 or n == 3:
            return []
        
        

        def backtrack(nums: List[int], sols: List[List[str]]):
            for b in filter(
                lambda b: all(
                    (b != q and p+b != q+len(nums) and p+q != b+len(nums) for p, q in enumerate(nums))
                ),
                range(n)
            ):
                if len(nums) == n - 1:
                    solutions.append([ "."*y + "Q" + "."*(n-y-1) for y in nums + [b] ])
                    return
                nums.append(b)
                backtrack(nums, sols)
                nums.pop()
        
        solutions = []
        for k in range(n):
            backtrack([k], solutions)
                        
        return solutions
