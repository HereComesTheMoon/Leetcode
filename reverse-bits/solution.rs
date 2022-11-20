impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        (0..32).fold((0, x), |acc, _| (acc.0 << 1 | acc.1 & 1, acc.1 >> 1)).0
    }
}