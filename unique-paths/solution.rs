impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        nchoosek(m + n - 2, n - 1)
    }
}

fn nchoosek(n: i32, k: i32) -> i32 {
    let k = if 2*k > n {
        (n - k) as u128
    } else {
        k as u128
    };

    let n = n as u128;

    ((n-k+1..=n).product::<u128>() / (1..=k).product::<u128>()) as i32
}