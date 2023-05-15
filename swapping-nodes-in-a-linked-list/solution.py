# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        n = 1
        while node is not None:
            node = node.next
            n += 1
        
        node_a = head
        for _ in range(k - 1):
            node_a = node_a.next
        
        node_b = head
        for _ in range(n - k - 1):
            node_b = node_b.next

        val = node_a.val
        node_a.val = node_b.val
        node_b.val = val
        return head
