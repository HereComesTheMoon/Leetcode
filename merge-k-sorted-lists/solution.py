# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
            if a is None:
                return b
            if b is None:
                return a
            if b.val < a.val:
                a, b = b, a
            head = a
            node = a
            a = a.next
            while a and b:
                if a.val < b.val:
                    node.next = a
                    node = a
                    a = a.next
                else:
                    node.next = b
                    node = b
                    b = b.next
            if a:
                node.next = a
            else:
                node.next = b
            return head

        main = None
        for x in lists:
            main = merge2Lists(main, x)

        return main
