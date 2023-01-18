class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        k = 1
        res = nums[0] + nums[1] + nums[2]
            
        for i in range(len(nums) - 2):
            j = len(nums) - 1
            k = i + 1
            while k < j:
                val = nums[i] + nums[j] + nums[k]
                if abs(target - val) < abs(target - res):
                    res = val
                if val < target:
                    k += 1
                elif val == target:
                    return target
                else:
                    j -= 1
        return res
