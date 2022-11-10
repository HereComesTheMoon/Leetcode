impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        nums.into_iter()
            .fold((0, 0), |acc, x| (acc.1, i32::max(acc.1, acc.0 + x)))
            .1
    }
}
