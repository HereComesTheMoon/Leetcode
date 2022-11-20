use std::collections::VecDeque;

impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut sol: Vec<i32> = Vec::with_capacity(matrix.len() * matrix[0].len());
        let mut matrix: VecDeque<VecDeque<i32>> =
            matrix.into_iter().map(|row| row.into()).collect();

        while !matrix.is_empty() && matrix[0].len() != 0 {
            sol.extend(matrix.pop_front().unwrap());
            for row in &mut matrix {
                sol.push(row.pop_back().unwrap());
            }
            if matrix.is_empty() || matrix[0].len() == 0 {
                break;
            }
            sol.extend(matrix.pop_back().unwrap().into_iter().rev());
            for row in &mut matrix.iter_mut().rev() {
                sol.extend(row.drain(0..=0));
            }
        }

        sol
    }
}
