# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = set()
        double = {}
        def rec(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return None
            l = rec(node.left)
            r = rec(node.right)
            rep = (node.val, l, r)
            if rep in seen:
                double[rep] = node
            else:
                seen.add(rep)
            return rep
        rec(root)
        return [node for node in double.values()]