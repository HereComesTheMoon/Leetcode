impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s = s.as_bytes();

        let mut i = match s.iter().position(|c| c.is_ascii_alphanumeric()) {
            Some(index) => index,
            _ => return true,
        };
        let mut j = s.iter().rposition(|c| c.is_ascii_alphanumeric()).unwrap();

        while i < j {
            while !s[i].is_ascii_alphanumeric() { i += 1 }
            while !s[j].is_ascii_alphanumeric() { j -= 1 }
            if s[i].to_ascii_lowercase() != s[j].to_ascii_lowercase() {
                return false
            }
            i += 1;
            j -= 1;
        }
        true
    }
}