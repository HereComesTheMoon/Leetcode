# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(node):
            if node.left is not None:
                yield from inorder(node.left)
            yield node.val
            if node.right is not None:
                yield from inorder(node.right)

        it = inorder(root)
        last = it.__next__()
        res = float('inf')
        for x in it:
            res = min(res, x - last)
            last = x
        return res