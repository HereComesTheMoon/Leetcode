# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return []
            vals = rec(node.left) + rec(node.right)
            if vals:
                for num in vals:
                    num.append(node.val)
                return vals
            return [[node.val]]
        
        nums = rec(root)
        return sum( sum( x * pow(10, k) for k, x in enumerate(num) ) for num in nums )