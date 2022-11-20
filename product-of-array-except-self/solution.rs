impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut sol = vec![1; nums.len()];

        let mut acc = 1;
        for (k, x) in nums.iter().enumerate() {
            sol[k] *= acc;
            acc *= *x;
        }
        acc = 1;
        for (k, x) in nums.iter().enumerate().rev() {
            sol[k] *= acc;
            acc *= *x;
        }
        sol
    }
}

