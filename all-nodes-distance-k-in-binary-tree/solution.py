# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = {}
        def search(node, par):
            d[node.val] = []
            if par is not None:
                d[node.val].append(par)
            if node.left is not None:
                d[node.val].append(node.left.val)
                search(node.left, node.val)
            if node.right is not None:
                d[node.val].append(node.right.val)
                search(node.right, node.val)

        search(root, None)
        seen = { target.val }
        border = { target.val }
        for _ in range(k):
            new_border = set()
            for node in border:
                for next_node in d[node]:
                    if next_node in seen:
                        continue
                    seen.add(next_node)
                    new_border.add(next_node)
            border = new_border
        return list(border)