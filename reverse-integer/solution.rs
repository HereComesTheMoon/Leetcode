impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let vals = build(x);
        let mut res = 0_i32;
        for x in vals {
            if let Some(new) = res.checked_mul(10) {
                res = new;
            } else { return 0; }
            if let Some(new) = res.checked_add(x) {
                res = new;
            } else { return 0; }
        }
        if x < 0 {
            res.checked_mul(-1).or(Some(0)).unwrap()
        } else {
            res
        }
    }
}

fn build(mut x: i32) -> Vec<i32> {
    let mut res = vec![];
    x = i32::abs(x);
    while x != 0 {
        res.push(x % 10);
        x /= 10;
    }
    res
}