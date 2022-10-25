impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut a = s.chars().rev().filter(|c| c.is_alphanumeric()).map(|c| c.to_ascii_lowercase());
        for x in s.chars().filter(|c| c.is_alphanumeric()).map(|c| c.to_ascii_lowercase()) {
            if x != a.next().unwrap() {
                return false
            }
        }
        true
    }
}