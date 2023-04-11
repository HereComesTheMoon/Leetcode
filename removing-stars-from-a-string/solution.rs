impl Solution {
    pub fn remove_stars(s: String) -> String {
        let s = s.as_bytes();
        let mut res = Vec::with_capacity(s.len());
        let mut stars = 0;
        for i in (0..s.len()).rev() {
            if s[i] == b'*' {
                stars += 1;
                continue
            } 
            if 0 < stars {
                stars -= 1;
                continue
            }
            res.push(s[i]);
        }
        res.reverse();
        String::from_utf8(res).unwrap()
    }
}