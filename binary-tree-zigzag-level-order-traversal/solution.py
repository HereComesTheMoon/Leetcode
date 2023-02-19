# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            res.append([])
            for _ in range(n):
                node = q.popleft()
                res[-1].append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        for k, level in enumerate(res):
            if k % 2:
                level.reverse()    
        return res
