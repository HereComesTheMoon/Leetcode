# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        assert len(inorder) == len(postorder)
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = postorder[-1]
        i = inorder.index(root)

        l = self.buildTree(inorder[:i], postorder[:i])
        r = self.buildTree(inorder[i+1:], postorder[i:len(postorder) - 1])
        return TreeNode(root, l, r)
