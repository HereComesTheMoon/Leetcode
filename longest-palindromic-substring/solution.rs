impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        if s.len() <= 1 {
            return s;
        }
        let s = s.as_bytes();
        let mut dp: Vec<Vec<bool>> = Vec::with_capacity(s.len());
        dp.push(vec![true; s.len()]);
        dp.push(vec![true; s.len()]);

        let mut longest = (0, 0);

        for window in 1..s.len() - 0 {
            let mut row = vec![false; s.len() - window];
            for i in 0..s.len() - window {
                if dp[window - 1][i + 1] && s[i] == s[i + window] {
                    row[i] = true;
                    longest = (i, i + window);
                }
            }
            dp.push(row);
        }
        std::str::from_utf8(&s[longest.0..=longest.1])
            .unwrap()
            .into()
    }
}
