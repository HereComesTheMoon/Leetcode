impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = vec![];
        for c in s.chars() {
            match c {
                '(' | '{' | '[' => stack.push(c),
                ')' => {
                    if let Some('(') = stack.pop() {
                    } else {
                        return false;
                    }
                },
                '}' => {
                    if let Some('{') = stack.pop() {
                    } else {
                        return false;
                    }
                },
                ']' => {
                    if let Some('[') = stack.pop() {
                    } else {
                        return false;
                    }
                },
                _ => unreachable!(),
            }
        }
        return stack.is_empty();
    }
}