class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        now = 0
        for x in gain:
            now += x
            res = max(res, now)
        return res