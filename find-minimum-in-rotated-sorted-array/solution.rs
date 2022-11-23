impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        if nums[0] <= *nums.last().unwrap() {
            return nums[0];
        }
        let first = nums[0];
        let mut i = 0;
        let mut j = nums.len();
        
        while i + 1 < j {
            if nums[(j + i) / 2] < first {
                j = (j + i) / 2;
            } else {
                i = (j + i) / 2;
            }
        }
        nums[(j + i + 1) / 2]
    }
}