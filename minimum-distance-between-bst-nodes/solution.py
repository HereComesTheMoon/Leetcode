# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            smallest, best, biggest = node.val, float('inf'), node.val
            if node.left is not None:
                lsm, lbe, lbi = rec(node.left)
                smallest = lsm
                best = min(best, lbe, node.val - lbi)
            if node.right is not None:
                rsm, rbe, rbi = rec(node.right)
                biggest = rbi
                best = min(best, rbe, rsm - node.val)
            return smallest, best, biggest
        return rec(root)[1]
            
        