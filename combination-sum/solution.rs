impl Solution {
    pub fn combination_sum(mut candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        candidates.sort_unstable();

        rec(&candidates, target)
    }
}

pub fn rec(cand: &[i32], target: i32) -> Vec<Vec<i32>> {
    if target < 0 || cand.is_empty() {
        return vec![];
    }
    if target == 0 {
        return vec![vec![]];
    }
    let a = rec(cand, target - cand[0]);
    let b = rec(&cand[1..], target);

    a.into_iter()
        .map(|mut sol| {
            sol.push(cand[0]);
            sol
        })
        .chain(b.into_iter())
        .collect()
}

