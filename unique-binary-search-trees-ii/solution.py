# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def rec(i, j):
            if i == j:
                return [None]
            res = []
            for k in range(i, j):
                l = rec(i, k)
                r = rec(k + 1, j)
                res.extend(
                    TreeNode(k, ll, rr) for ll in l for rr in r
                )
            return res
        return rec(1, n + 1)