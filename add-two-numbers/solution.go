/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var head ListNode = ListNode{l1.Val + l2.Val, nil}
    carry := head.Val / 10
    head.Val %= 10

    var lastNode *ListNode = &head

    l1 = l1.Next
    l2 = l2.Next

    for l1 != nil && l2 != nil {
        val := l1.Val + l2.Val + carry
        var node ListNode = ListNode{val % 10, nil}
        carry = val / 10
        lastNode.Next = &node
        lastNode = &node
        l1 = l1.Next
        l2 = l2.Next
    }

    if l2 != nil {
        l1, l2 = l2, l1
    }

    // Let us try something dumb. Once one of the two lists is finished, just append the remaining numbers with minor changes
    if l1 != nil {
        lastNode.Next = l1
        for l1 != nil {
            if carry == 0 {
                break
            }

            l1.Val++
            carry = l1.Val / 10
            l1.Val %= 10

            lastNode = l1
            l1 = l1.Next
        }

        // assert l1 == nil
        if carry != 0 {
            var node ListNode = ListNode{1, nil}
            lastNode.Next = &node
        }
    }

    // assert l1 == nil && l2 == nil
    if carry != 0 {
        var node ListNode = ListNode{1, nil}
        lastNode.Next = &node
    }

    return &head
}
