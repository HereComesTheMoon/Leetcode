# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        def rec(root, sol):
            if root is None:
                return
            rec(root.left, sol)
            sol.append(root.val)
            rec(root.right, sol)
        
        res = []
        rec(root, res)
            
        return res
        