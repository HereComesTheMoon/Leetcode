// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
type Node = Option<Box<ListNode>>;

impl Solution {
    pub fn remove_nth_from_end(mut head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let len = length(&head);
        if len == n as usize {
            return head.unwrap().next;
        }

        let mut ptr = head.as_mut();
        for _ in 1..len - (n as usize) {
            ptr = ptr.unwrap().next.as_mut();
        }

        let temp = std::mem::take(&mut ptr.as_mut().unwrap().next);
        if let Some(node) = temp {
            ptr.unwrap().next = node.next;
        }
        head
    }
}

pub fn length(mut head: &Node) -> usize {
    let mut count = 0;
    while let Some(node) = head {
        count += 1;
        head = &node.next;
    }
    count
}

