from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        largest_sum = float('-inf')
        level = 1
        current_level = 1
        while q:
            val = 0
            for _ in range(len(q)):
                node = q.popleft()
                val += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if largest_sum < val:
                level = current_level
                largest_sum = val
            current_level += 1
        return level