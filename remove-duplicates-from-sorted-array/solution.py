class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        prev = nums[0]
        for x in nums[1:]:
            if x != prev:
                nums[count] = x
                count += 1
                prev = x
        return count
        