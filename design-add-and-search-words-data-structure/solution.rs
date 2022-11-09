
struct WordDictionary {
    head: Box<Node>,
}

struct Node {
    next: [Option<Box<Node>>; 26],
    word: bool,
}

impl Node {
    fn new() -> Box<Node> {
        Box::new(Node {
            next: [
                None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None,
            ],
            word: false,
        })
    }
}

impl WordDictionary {
    fn new() -> Self {
        WordDictionary { head: Node::new() }
    }

    fn add_word(&mut self, word: String) {
        let mut n = &mut self.head;
        for &c in word.as_bytes() {
            if let None = n.next[(c - b'a') as usize] {
                n.next[(c - b'a') as usize] = Some(Node::new());
            }
            n = n.next[(c - b'a') as usize].as_mut().unwrap();
        }
        n.word = true;
    }

    fn search(&self, word: String) -> bool {
        self.head.search(word.as_bytes())
    }
}

impl Node {
    fn search(&self, word: &[u8]) -> bool {
        if word.len() == 0 {
            return self.word;
        }
        if word[0] == b'.' {
            for n in &self.next {
                if let Some(n) = n {
                    if n.search(&word[1..]) {
                        return true;
                    }
                }
            }
            return false;
        }
        if let Some(n) = &self.next[(word[0] - b'a') as usize].as_ref() {
            n.search(&word[1..])
        } else {
            false
        }
    }
}

