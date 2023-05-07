class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        perimeter = sum(nums)
        if perimeter % 4 != 0:
            return False
        length = perimeter // 4
        nums.sort(reverse=True)
        if length < nums[0]:
            return False

        sides = [0] * 4

        def rec(k: int):
            if k == len(nums):
                return sides[0] == sides[1] == sides[2] == sides[3]
            for i in range(4):
                if length < sides[i] + nums[k]:
                    continue
                sides[i] += nums[k]
                if rec(k + 1):
                    return True
                sides[i] -= nums[k]
        
        return rec(0)





