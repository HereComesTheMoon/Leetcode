class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        result = 0
        
        # for x in filter(lambda x: x - 1 not in vals, nums):
        for x in vals:
            if x - 1 in vals:
                continue
                
            current = 0
            while x in vals:
                current += 1
                x += 1

            result = max(result, current)
            
        return result
            
            
        