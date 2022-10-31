class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        a = 1
        b = 1
        for k in range(len(nums)):
            result[k] *= a
            a *= nums[k]
            
            result[-k-1] *= b
            b *= nums[-k-1]
        
        return result
            
            
        
        