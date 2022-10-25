// This one was horrible. I tried to get way too clever at first. Confusing!
use std::cmp::Ordering;
impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();

        let mut res: Vec<Vec<i32>> = Vec::with_capacity(nums.len()/3 + 1);

        for (i, &x) in nums.iter().enumerate() {
            let mut a = i + 1;
            let mut b = nums.len() - 1;
            if 0 < i && nums[i-1] == nums[i] {
                continue
            }

            while a < b {
                match (nums[a] + nums[b]).partial_cmp(&-x).unwrap() {
                    Ordering::Equal => {
                        let next = vec![x, nums[a], nums[b]];
                        while a < b && nums[a] == next[1] { a += 1 }
                        while a < b && nums[b] == next[2] { b -= 1 }
                        res.push(next);
                    },
                    Ordering::Less => a += 1,
                    Ordering::Greater => b -= 1,
                }
            }
        }

        res
    }
}
