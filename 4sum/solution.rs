use std::collections::HashSet;

impl Solution {
    pub fn four_sum(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res = HashSet::new();
        nums.sort_unstable();
        let n = nums.len();
        for a in 0..n {
            for b in (a+1)..n {
                for c in (b+1)..n {
                    let goal = target - nums[a] - nums[b] - nums[c];
                    if let Ok(dd) = nums[(c+1)..n].binary_search(&goal) {
                        let mut x = 0_i32;
                        x = if let Some(val) = x.checked_add(nums[a]) {
                            val
                        } else { continue };
                        x = if let Some(val) = x.checked_add(nums[b]) {
                            val
                        } else { continue };
                        x = if let Some(val) = x.checked_add(nums[c]) {
                            val
                        } else { continue };
                        x = if let Some(val) = x.checked_add(nums[c + 1 + dd]) {
                            val
                        } else { continue };
                        res.insert(vec![nums[a], nums[b], nums[c], nums[c + 1 + dd]]);
                    }

                }
            }
        }
        res.drain().collect()
    }
}