class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in temperatures]
        for k0, t0 in reversed(list(enumerate(temperatures))):
            while stack:
                k1, t1 = stack[-1]
                if t1 <= t0:
                    stack.pop()
                    continue
                res[k0] = k1 - k0
                break
            stack.append((k0, t0))
        return res
            