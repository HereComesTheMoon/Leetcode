# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        assert -100_000 <= root.val
        return rec(root, -100_000)

def rec(root: TreeNode, biggest: int) -> int:
    res = 0
    if biggest <= root.val:
        res += 1
    if root.left is not None:
        res += rec(root.left, max(biggest, root.val))
    if root.right is not None:
        res += rec(root.right, max(biggest, root.val))
    return res