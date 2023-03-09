# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while True:
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            slow = slow.next
            if fast == slow:
                break
        node = head
        while node != slow:
            node = node.next
            slow = slow.next
        return node
