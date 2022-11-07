type Trie struct {
	next     [26]*Trie
	terminal bool
}

func Constructor() Trie {
	return Trie{
		next:     [26]*Trie{},
		terminal: false,
	}
}

func (this *Trie) Insert(word string) {
	if word == "" {
		this.terminal = true
		return
	}
	if this.next[word[0]-'a'] == nil {
		a := Constructor()
		this.next[word[0]-'a'] = &a
	}
	this.next[word[0]-'a'].Insert(word[1:])
}

func (this *Trie) Search(word string) bool {
	if word == "" {
		return this.terminal
	}
	if this.next[word[0]-'a'] == nil {
		return false
	}
	return this.next[word[0]-'a'].Search(word[1:])
}

func (this *Trie) StartsWith(prefix string) bool {
	if prefix == "" {
		return true
	}
	if this.next[prefix[0]-'a'] == nil {
		return false
	}
	return this.next[prefix[0]-'a'].StartsWith(prefix[1:])
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
