impl Solution {
    pub fn hammingWeight (n: u32) -> i32 {
        [
            2_u32.pow(0) & n != 0,
            2_u32.pow(1) & n != 0,
            2_u32.pow(2) & n != 0,
            2_u32.pow(3) & n != 0,
            2_u32.pow(4) & n != 0,
            2_u32.pow(5) & n != 0,
            2_u32.pow(6) & n != 0,
            2_u32.pow(7) & n != 0,
            2_u32.pow(8) & n != 0,
            2_u32.pow(9) & n != 0,
            2_u32.pow(10) & n != 0,
            2_u32.pow(11) & n != 0,
            2_u32.pow(12) & n != 0,
            2_u32.pow(13) & n != 0,
            2_u32.pow(14) & n != 0,
            2_u32.pow(15) & n != 0,
            2_u32.pow(16) & n != 0,
            2_u32.pow(17) & n != 0,
            2_u32.pow(18) & n != 0,
            2_u32.pow(19) & n != 0,
            2_u32.pow(20) & n != 0,
            2_u32.pow(21) & n != 0,
            2_u32.pow(22) & n != 0,
            2_u32.pow(23) & n != 0,
            2_u32.pow(24) & n != 0,
            2_u32.pow(25) & n != 0,
            2_u32.pow(26) & n != 0,
            2_u32.pow(27) & n != 0,
            2_u32.pow(28) & n != 0,
            2_u32.pow(29) & n != 0,
            2_u32.pow(30) & n != 0,
            2_u32.pow(31) & n != 0,
        ].into_iter().filter(|&&b| b).count() as i32
    }
}

