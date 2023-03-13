# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        stackl = [root.left]
        stackr = [root.right]
        while stackl and stackr:
            l = stackl.pop()
            r = stackr.pop()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            stackl.append(l.left)
            stackl.append(l.right)
            stackr.append(r.right)
            stackr.append(r.left)

        return stackl == stackr            