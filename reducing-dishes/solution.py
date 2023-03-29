class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        comp = sum(satisfaction)
        i = 0
        while comp < 0:
            comp -= satisfaction[i]
            i += 1
        return sum(k * x for k, x in enumerate(satisfaction[i:], 1))
