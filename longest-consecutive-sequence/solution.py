class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        result = 0
        while vals:
            x = vals.pop()
            vals.add(x)

            while x-1 in vals:
                x = x - 1
            
            current = 0
            while x in vals:
                vals.discard(x)
                current += 1
                x = x + 1
                
            result = max(result, current)
        return result
            
            
        