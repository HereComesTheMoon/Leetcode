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
impl Solution {
    pub fn merge_two_lists(mut a: Option<Box<ListNode>>, mut b: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
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
            break
        }
        if a.as_ref().unwrap().next.is_none() {
            a.as_mut().unwrap().next = b;
            break
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
}