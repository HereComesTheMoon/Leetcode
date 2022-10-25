impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let lower = intervals.partition_point(|intval| intval[0] < new_interval[0]);

        let mut niv = new_interval;
        
        let upper = intervals[lower..]
            .iter()
            .position(|intval| niv[1] < intval[0])
            .map(|x| x + lower)
            .unwrap_or(intervals.len());

        niv[1] = niv[1].max(intervals.get(upper-1).unwrap_or(&niv)[1]);
        
        let mut res: Vec<Vec<i32>> = Vec::with_capacity(lower + intervals.len() - upper + 1);

        if 0 < lower {
            res.extend(intervals[..lower-1].to_vec());
            if niv[0] <= intervals[lower-1][1] {
                res.extend(vec![vec![intervals[lower-1][0], niv[1].max(intervals[lower-1][1])]]);
            } else {
                res.extend(vec![intervals[lower-1].to_owned(), niv]);
            }
        } else {
            res.extend(vec![niv]);
        }
        res.extend(intervals[upper..].to_owned());
        res
    }
}
