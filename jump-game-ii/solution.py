class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        border = 0
        highest = -1
        steps = 0
        pos = -1
        while highest < len(nums) - 1:
            pos += 1
            highest = max(highest, pos + nums[pos])
            if pos == border:
                steps += 1
                border = highest
        print(f"{pos=}, {border=}, {highest=}")
        return steps + (1 if highest != border else 0)