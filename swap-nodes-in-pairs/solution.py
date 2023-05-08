# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        a = head
        head = a.next
        next_a = a.next.next
        a.next.next = a
        a.next = next_a
        prev = a
        a = next_a

        while a is not None and a.next is not None:
            prev.next = a.next
            next_a = a.next.next
            a.next.next = a
            a.next = next_a
            prev = a
            a = next_a

        return head
        