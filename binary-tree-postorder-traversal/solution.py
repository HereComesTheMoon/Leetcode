# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def rec(node):
            if node is None:
                return None
            yield from rec(node.left)
            yield from rec(node.right)
            yield node.val
        
        return rec(root)