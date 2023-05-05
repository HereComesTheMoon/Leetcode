from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([(root, 0)])
        res = 0
        while q:
            now, pos = q.popleft()
            small = pos
            n = len(q)
            if now.left is not None:
                q.append((now.left, 2*pos))
            if now.right is not None:
                q.append((now.right, 2*pos + 1))
            large = pos
            for _ in range(n):
                now, pos = q.popleft()
                if now.left is not None:
                    q.append((now.left, 2*pos))
                if now.right is not None:
                    q.append((now.right, 2*pos + 1))
                large = max(large, pos)
            res = max(res, large - small)
        return res + 1
                

        