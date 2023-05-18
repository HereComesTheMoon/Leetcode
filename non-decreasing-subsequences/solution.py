from functools import cache

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        dp = [[] for _ in range(n)]
        for k in range(n):
            for j in range(k):
                if nums[j] <= nums[k]:
                    dp[k].extend(row + [nums[k]] for row in dp[j])
                    dp[k].append([nums[j], nums[k]])
        
        return list({tuple(x) for row in dp for x in row})