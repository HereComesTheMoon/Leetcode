// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        helper(&p, &q)
    }
}

pub fn helper(p: &Option<Rc<RefCell<TreeNode>>>, q: &Option<Rc<RefCell<TreeNode>>>) -> bool {
    if p.is_none() != q.is_none() {
        return false;
    }
    if p.is_none() {
        return true;
    }
    let p = p.as_ref().unwrap();
    let q = q.as_ref().unwrap();
    if p.borrow().val != q.borrow().val {
        return false;
    }
    return helper(&p.borrow().left, &q.borrow().left)
        && helper(&p.borrow().right, &q.borrow().right);
}

