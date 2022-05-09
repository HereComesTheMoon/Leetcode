# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxval = 1
        stack = [(root, 1)]
        while stack:
            nxt, val = stack.pop()
            maxval = max(maxval, val)
            if nxt.left:
                stack.append((nxt.left, val + 1))
            if nxt.right:
                stack.append((nxt.right, val + 1))

        return maxval
                