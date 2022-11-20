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

use std::collections::VecDeque;

impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        if lists.is_empty() {
            return None;
        }
        let mut lists: VecDeque<Node> = lists.into();
        while lists.len() > 1 {
            let a = lists.pop_back().unwrap();
            let b = lists.pop_back().unwrap();
            lists.push_front(merge(a, b));
        }

        lists.pop_back().unwrap()
    }
}

pub fn merge(mut a: Node, mut b: Node) -> Node {
    if a.is_none() {
        return b;
    }
    if b.is_none() {
        return a;
    }
    if a.as_ref().unwrap().val > b.as_ref().unwrap().val {
        std::mem::swap(&mut a, &mut b);
    }

    let mut head = a;
    let mut a = head.as_mut();

    while a.is_some() {
        if b.is_none() {
            break;
        }
        if a.as_ref().unwrap().next.is_none() {
            a.as_mut().unwrap().next = b;
            break;
        }
        if a.as_ref().unwrap().next.as_ref().unwrap().val < b.as_ref().unwrap().val {
            a = a.unwrap().next.as_mut();
        } else {
            std::mem::swap(&mut a.as_mut().unwrap().next, &mut b);
            a = a.unwrap().next.as_mut();
        }
    }

    head
}

