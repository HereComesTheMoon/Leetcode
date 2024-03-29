use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<[u8; 26], Vec<String>> = HashMap::new();

        for s in strs {
            let mut b = [0_u8; 26];

            for &c in s.as_bytes() {
                b[(c - b'a') as usize] += 1;
            }

            if let Some(v) = groups.get_mut(&b) {
                v.push(s);
            } else {
                groups.insert(b, vec![s]);
            }
        }

        groups.into_values().collect()
    }
}
