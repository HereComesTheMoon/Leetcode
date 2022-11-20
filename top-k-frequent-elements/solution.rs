use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut count: HashMap<i32, usize> = HashMap::with_capacity(nums.len());
        for &x in nums.iter() {
            if let Some(val) = count.get_mut(&x) {
                *val += 1;
            } else {
                count.insert(x, 1);
            }
        }

        let mut nums: Vec<(usize, i32)> = count.into_iter().map(|(k, v)| (v, k)).collect();
        nums.sort_unstable();

        nums[nums.len() - k as usize..]
            .into_iter()
            .map(|&(_, v)| v)
            .collect()
    }
}

