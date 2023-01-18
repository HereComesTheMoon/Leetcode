class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head

        counter = 1
        last = head
        while last.next is not None:
            counter += 1
            last = last.next

        k = k % counter
        if k == 0:
            return head

        new_last = head
        for _ in range(counter - k - 1):
            new_last = new_last.next

        new_head = new_last.next
        new_last.next = None

        last.next = head

        return new_head
