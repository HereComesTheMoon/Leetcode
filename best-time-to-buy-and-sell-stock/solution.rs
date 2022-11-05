impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len() <= 1 { return 0 }

        let mut buy = prices[0];
        let mut profit = 0;

        for sell in prices {
            profit = profit.max(sell - buy);
            buy = buy.min(sell);
        }

        profit
    }
}
