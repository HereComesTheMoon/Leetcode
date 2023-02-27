"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return build(grid, 0, 0, len(grid))


def build(grid: List[List[int]], x, y, w) -> 'Node':
    if w == 1:
        return Node(grid[y][x], True, None, None, None, None)
    tl = build(grid, x, y, w // 2)
    tr = build(grid, x + w // 2, y, w // 2)
    bl = build(grid, x, y + w // 2, w // 2)
    br = build(grid, x + w // 2, y + w // 2, w // 2)
    just_leaves = tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
    same_values = tl.val == tr.val == bl.val == br.val
    if just_leaves and same_values:
        return Node(tl.val, True, None, None, None, None)
    return Node(grid[y][x], False, tl, tr, bl, br)
