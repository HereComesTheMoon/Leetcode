# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if node.left is None and node.right is None:
                return (node.val, 0)
            if node.left is None:
                val, depth = rec(node.right)
                return val, depth + 1
            if node.right is None:
                val, depth = rec(node.left)
                return val, depth + 1
            lval, ldepth = rec(node.left)
            rval, rdepth = rec(node.right)
            if ldepth < rdepth:
                return rval, rdepth +1
            else:
                return lval, ldepth + 1
        
        return rec(root)[0]