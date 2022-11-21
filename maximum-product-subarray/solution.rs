impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        if nums.len() <= 1 { return nums[0]; }
        let mut pos = 0;
        let mut neg = 0;
        let mut res = i32::MIN;
        
        for x in nums {
            if x < 0 {
                std::mem::swap(&mut pos, &mut neg);
            }
            pos = i32::max(pos*x, x);
            neg = i32::min(neg*x, x);
            res = res.max(pos);
        }
        
        res
    }
}