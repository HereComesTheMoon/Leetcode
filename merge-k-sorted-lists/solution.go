/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

import "container/heap"

type NodeHeap []*ListNode

func (h NodeHeap) Len()          int  { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h NodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *NodeHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func (h *NodeHeap) Push(x interface{}) {
    *h = append(*h, x.(*ListNode))
}

func mergeKLists(lists []*ListNode) *ListNode {
    filtered := make([]*ListNode, 0, len(lists))
    for _, v := range lists {
        if v != nil {
            filtered = append(filtered, v)
        }
    }
    if len(filtered) == 0 {
        return nil
    }
    var hh NodeHeap = filtered
    h := &hh
    heap.Init(h)
    head := heap.Pop(h).(*ListNode)
    now := head

    for h.Len() > 0 {
        next := heap.Pop(h).(*ListNode)
        for now.Next != nil && now.Next.Val <= next.Val {
            now = now.Next
        }
        if now.Next != nil {
            heap.Push(h, now.Next)
        }
        now.Next = next
    }
    return head
}


