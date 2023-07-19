impl Solution {
    pub fn erase_overlap_intervals(mut v: Vec<Vec<i32>>) -> i32 {
        v.sort();

        for now in 0..v.len() - 1 {
            if v[now][1] <= v[now + 1][0] {
                continue;
            }
            if v[now][1] <= v[now + 1][1] {
                v.swap(now, now + 1);
            }
            v[now][0] = 0;
            v[now][1] = -1;
        }

        v.into_iter().filter(|v| v[0] > v[1]).count() as i32
    }
}