impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        for r in 0..matrix.len() / 2 {
            for i in 0..matrix.len() - 1 - 2 * r {
                rot(matrix, r, i);
            }
        }
    }
}

#[inline]
pub fn rot(m: &mut Vec<Vec<i32>>, r: usize, i: usize) {
    let l = m.len();
    let n = m[0].len();

    let mut temp = m[r][r + i];
    temp = std::mem::replace(&mut m[r + i][n - 1 - r], temp);
    temp = std::mem::replace(&mut m[l - 1 - r][n - 1 - i - r], temp);
    temp = std::mem::replace(&mut m[l - 1 - r - i][r], temp);
    m[r][r + i] = temp;
}
