impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        let res = (n as f64).log(3.0);
        return (res - (res.round() as f64)).abs() < 0.0000000000001;
    }
}
