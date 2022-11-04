impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut reachable = 0;
        for i in (0..nums.len()-1) {
            reachable = reachable.max(i + nums[i] as usize);
            if reachable <= i {
                return false;
            }
            if nums.len() - 1 <= reachable {
                return true;
            }
        }
        true
    }
}