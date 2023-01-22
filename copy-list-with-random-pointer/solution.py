"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        d: dict[Node, Node] = { None: None }
        node = head
        while node is not None:
            d[node] = Node(node.val)
            node = node.next
        node = head
        while node is not None:
            d[node].next = d[node.next]
            d[node].random = d[node.random]
            node = node.next
        return d[head]
        