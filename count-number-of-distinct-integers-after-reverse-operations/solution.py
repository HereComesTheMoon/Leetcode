class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(
            nums + [int("".join(reversed(str(x)))) for x in nums]
        ))