impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        
        (0..nums.len()-1)
            .rev()
            .fold(nums.len() - 1, |need_to_reach, i|
                if i + nums[i] as usize >= need_to_reach {
                    i
                } else {
                    need_to_reach
                }) <= nums[0] as usize
    }
}