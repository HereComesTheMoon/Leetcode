from random import randrange

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.root = head
        

    def getRandom(self) -> int:
        pick = self.root
        node = self.root.next
        count = 1
        while node is not None:
            if randrange(0, count + 1) == 0:
                pick = node
            node = node.next
            count += 1
        return pick.val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()