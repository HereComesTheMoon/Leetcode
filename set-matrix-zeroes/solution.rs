use std::collections::HashSet;
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut rows: HashSet<usize> = HashSet::with_capacity(matrix.len());
        let mut cols: HashSet<usize> = HashSet::with_capacity(matrix[0].len());

        for y in 0..matrix.len() {
            for x in 0..matrix[0].len() {
                if matrix[y][x] == 0 {
                    rows.insert(y);
                    cols.insert(x);
                }
            }
        }


        for y in rows.into_iter() {
            for item in &mut matrix[y] { *item = 0 };
        }

        for x in cols.into_iter() {
            for y in 0..matrix.len() {
                matrix[y][x] = 0;
            }
        }

    }
}
