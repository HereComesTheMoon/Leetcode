# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        expected = 1
        none_seen = False
        while q:
            if len(q) != expected:
                break
            for _ in range(expected):
                node = q.popleft()
                if none_seen and node is not None:
                    return False
                if node is None:
                    none_seen = True
                    continue
                q.append(node.left)
                q.append(node.right)
            if none_seen:
                break
            expected *= 2
        return all(node is None for node in q)        