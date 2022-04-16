class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort(reverse=True)
        return self.solve(candidates, target)

    def solve(self, candidates: list[int], target: int) -> list[list[int]]:
        if len(candidates) == 1:
            if target % candidates[0] == 0:
                return [[candidates[0]] * (target//candidates[0])]
            else:
                return []
        solutions = []
        x = candidates[0]
        for k in (k for k in range(target//x + 1)):
            sols = self.solve(candidates[1:], target - k * x)
            solutions.extend([sol + [x] * k for sol in sols])
        return solutions
