impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if &num1 == "0" || &num2 == "0" {
            return "0".into();
        }
        let num1 = num1
            .as_bytes()
            .into_iter()
            .rev()
            .map(|&c| (c - b'0') as u32)
            .collect::<Vec<_>>();
        let num2 = num2
            .as_bytes()
            .into_iter()
            .rev()
            .map(|&c| (c - b'0') as u32)
            .collect::<Vec<_>>();

        let mut res = vec![0; num1.len() + num2.len()];
        for (i, x) in num1.iter().enumerate() {
            for (j, y) in num2.iter().enumerate() {
                for (k, z) in (x * y)
                    .to_string()
                    .as_bytes()
                    .into_iter()
                    .rev()
                    .map(|c| (c - b'0') as u32)
                    .enumerate() {
                    res[i + j + k] += z;
                }

            }
        }
        for i in 0..res.len() - 1 {
            res[i + 1] += res[i] / 10;
            res[i] %= 10;
        }

        res
            .into_iter()
            .rev()
            .skip_while(|&c| c == 0)
            .map(|c| char::from_digit(c, 10).unwrap())
            .collect()
    }
}