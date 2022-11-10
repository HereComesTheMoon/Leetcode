impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }
        let mut acc1 = (0, nums[0]);
        let mut acc2 = (0, nums[1]);
        for i in 1..nums.len() - 1 {
            acc1 = (acc1.1, i32::max(acc1.1, acc1.0 + nums[i]));
            acc2 = (acc2.1, i32::max(acc2.1, acc2.0 + nums[i + 1]));
        }
        i32::max(acc1.1, acc2.1)
    }
}
