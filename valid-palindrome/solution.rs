impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut a = s
            .as_bytes()
            .into_iter()
            .rev()
            .filter(|c| c
                    .is_ascii_alphanumeric())
            .map(|c| c
                 .to_ascii_lowercase());

        for x in s.as_bytes().into_iter().filter(|c| c.is_ascii_alphanumeric()).map(|c| c.to_ascii_lowercase()) {
            if x != a.next().unwrap() {
                return false
            }
        }

        true
    }
}