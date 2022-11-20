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
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let len = length(head);
        if len <= 2 {
            return;
        }

        let mut ptr: Option<&mut Box<ListNode>> = head.as_mut();
        for _ in 0..(len-1) / 2 {
            if let Some(node) = ptr {
                ptr = node.next.as_mut();
            }
        }

        let half = std::mem::take(&mut ptr.unwrap().next);
        let half = rev(half);

        merge(head, half);
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

pub fn rev(mut head: Node) -> Node {
    let mut last = None;
    loop {
        if head.is_none() {
            return last;
        }
        std::mem::swap(&mut head.as_mut().unwrap().next, &mut last);
        std::mem::swap(&mut head, &mut last);
    }
}

pub fn merge(mut left: &mut Node, mut right: Node) {
    loop {
        if left.is_none() {
            return;
        }
        std::mem::swap(&mut left.as_mut().unwrap().next, &mut right);
        left = &mut left.as_mut().unwrap().next;
    }
}

