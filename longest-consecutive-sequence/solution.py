class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        result = 0
        
        for x in filter(lambda x: x - 1 not in vals, nums):
            current = 0
            while x in vals:
                current += 1
                x = x + 1
            result = max(result, current)
            
        return result
            
            
        