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
    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut a = p.unwrap().as_ref().borrow().val;
        let mut c = q.unwrap().as_ref().borrow().val;
        if c < a {
            std::mem::swap(&mut a, &mut c);
        }

        fn helper(root: Option<Rc<RefCell<TreeNode>>>, p: i32, q: i32) -> Option<Rc<RefCell<TreeNode>>> {
            let val = root.as_ref().unwrap().as_ref().borrow().val;
            if p <= val && val <= q {
                return root;
            }
            if p < val {
                let l = root.unwrap().as_ref().borrow().left.clone();
                return helper(l, p, q);
            }
            let r = root.unwrap().as_ref().borrow().right.clone();
            return helper(r, p, q);
        }

        helper(root, a, c)
    }
}
