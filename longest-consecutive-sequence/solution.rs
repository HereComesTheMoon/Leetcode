use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let bag: HashSet<i32> = nums.into_iter().collect();
        
        let mut longest = 0;
        for x in bag.iter() {
            if !bag.contains(&(x - 1)) {
                let mut run = 1;
                let mut x = x + 1;
                while bag.contains(&x) {
                    x += 1;
                    run += 1;
                }
                longest = longest.max(run);
            }
        }
        longest
    }
}
