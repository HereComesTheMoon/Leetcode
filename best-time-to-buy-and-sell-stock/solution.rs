impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices.into_iter().fold((0, i32::MAX), 
        |acc, x| (i32::max(acc.0, x - acc.1), i32::min(acc.1, x))).0
    }
}