from functools import cache

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def rec(i: int, j: int) -> int:
            match (i, j, nums1[i] == nums2[j]):
                case (0, 0, _):
                    return int(nums1[i] == nums2[j])
                case (0, _, True) | (_, 0, True):
                    return 1
                case (0, _, False):
                    return rec(0, j - 1)
                case (_, 0, False):
                    return rec(i - 1, 0)
                case (_, _, True):
                    return 1 + rec(i - 1, j - 1)
                case _:
                    return max(
                        rec(i - 1, j),
                        rec(i, j - 1)
                    )
        
        return rec(len(nums1) - 1, len(nums2) - 1)