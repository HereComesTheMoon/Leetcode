class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if all(x == val for x in nums):
            return 0
        a, b = 0, len(nums) - 1
        while a < b:
            while a < b and nums[b] == val:
                b -= 1
            while a < b and nums[a] != val:
                a += 1
            if a < b:
                nums[a], nums[b] = nums[b], nums[a]
            else:
                return a + 1
            
            
            