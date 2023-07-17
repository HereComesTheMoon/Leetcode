# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = int("".join(str(x) for x in grabber(l1)))
        val2 = int("".join(str(x) for x in grabber(l2)))
        val = val1 + val2
        return builder(x for x in str(val))


def grabber(node):
    while node is not None:
        yield node.val
        node = node.next

def builder(it):
    if not it:
        return None
    head = ListNode(it.__next__())
    last = head
    for x in it:
        last.next = ListNode(x)
        last = last.next
    return head
