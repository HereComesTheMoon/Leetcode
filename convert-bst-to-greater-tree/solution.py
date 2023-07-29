# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(root, val):
            if root is None:
                return val
            rval = rec(root.right, val)
            root.val += rval
            lval = rec(root.left, root.val)
            return lval
        
        rec(root, 0)
        return root

