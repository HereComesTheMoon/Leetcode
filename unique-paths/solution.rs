impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        nchoosek(m + n - 2, n - 1)
    }
}

fn nchoosek(n: i32, k: i32) -> i32 {
    let k = if 2*k > n {
        n - k
    } else {
        k
    };
    let n = n as f64 + 1.;
    
    (1..=k).map(|i| i as f64).fold(1.0, |fin, i| fin * (n-i) / i).round() as i32
}