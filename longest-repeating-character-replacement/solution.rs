impl Solution {
    pub fn character_replacement(s: String, mut k: i32) -> i32 {
        if (k + 1)  as usize >= s.len() {
            return s.len() as i32
        }
        let s = s.as_bytes();
        let mut counter: [i32; 26] = [0; 26];
        for x in s.into_iter().map(|x| (x - b'A') as usize) {
            counter[x] += 1;           
        }
        let mut counter: Vec<(usize, i32)> = counter.iter().enumerate().filter(|(_, &x)| x > 0).map(|(a,b)| (a, *b)).collect();
        counter.sort_by_key(|item| -item.1);
        
        let mut biggest: usize = 0;
        
        for (letter, count) in counter {
            if count + k <= biggest as i32 {
                break
            }
            let mut i = 0;
            let mut used = 0;
            for (j, x) in s.iter().enumerate().map(|(j, x)| (j + 1, x)) {                
                let x = (x - b'A') as usize;
                if x != letter {
                    used += 1;
                    while k < used && i < j {
                        if ((s[i] - b'A') as usize) != letter {
                            used -= 1;
                        }
                        i += 1;
                    }
                }
                biggest = biggest.max(j - i);
            }
        }
        biggest as i32
    }
    
}

