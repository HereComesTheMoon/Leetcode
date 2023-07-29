# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(lower:int , upper: int) -> Optional[TreeNode]:
            if lower == upper:
                return None
            pos = max(range(lower, upper), key=lambda i: nums[i])

            l = rec(lower, pos)
            r = rec(pos + 1, upper)
            return TreeNode(nums[pos], l, r)
        
        return rec(0, len(nums))
