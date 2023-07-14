class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = defaultdict(int)
        for x in arr:
            d[x] = d[x - difference] + 1
        return max(d.values())
