# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def rec(node):
            if node is None:
                return None

            node.left = rec(node.left)
            node.right = rec(node.right)            
            if node.val == 1 or node.left is not None or node.right is not None:
                return node
            return None
        
        return rec(root)

