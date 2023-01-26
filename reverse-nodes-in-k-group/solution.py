class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head

        prec = None
        node = head
        while node is not None:
            succ = reverse_k(node, k)
            if succ is None:
                break
            if prec is None:
                head = succ
            else:
                prec.next = succ
            prec = node
            node = node.next
        return head

def reverse_k(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head is None:
        return None

    node = head
    for _ in range(k - 1):
        node = node.next
        if node is None:
            return None

    node = head
    prec = None
    succ = node.next
    for _ in range(k):
        succ = node.next
        node.next = prec
        prec = node
        node = succ

    head.next = node
    return prec
