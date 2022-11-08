
impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut v = vec![0_i32; n + 1];
        let mut k = 1;
        let mut boundary = 1;
        while k <= n {
            v[k] = v[k % boundary] + 1;
            k += 1;

            if k == 2*boundary {
                boundary *= 2;
            }
        }

        v
    }
}
