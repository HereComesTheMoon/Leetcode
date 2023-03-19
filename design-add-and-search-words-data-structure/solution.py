from string import ascii_lowercase

class WordDictionary:
    END = 'END'

    def __init__(self):
        self.d = {}        

    def addWord(self, word: str) -> None:
        d = self.d
        for c in word:
            dd = d.get(c, None)
            if dd is None:
                d[c] = {}
            d = d[c]
        d[WordDictionary.END] = True
        
    def search(self, word: str) -> bool:
        return WordDictionary.rec(self.d, word)

    def rec(d: dict, word: str) -> bool:
        if d is None:
            return False
        if not word:
            return d.get(WordDictionary.END, False)
        if word[0] == '.':
            return any(WordDictionary.rec(d.get(c, None), word[1:]) for c in ascii_lowercase)
        return WordDictionary.rec(d.get(word[0], None), word[1:])
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)