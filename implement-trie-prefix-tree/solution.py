class Node:
    def __init__(self):
        self.d = {}
        self.end = False

class Trie:
    def __init__(self):
        self.node = Node()

    def search(self, word) -> bool:
        n = self.node
        # warning, word might not be a string. It could be an iterator of arbitrary hashable keys. This is a usecase
        for c in word:
            if n is None:
                return False
            n = n.d.get(c, None)

        if n is None:
            return False
        return n.end

    def startsWith(self, word) -> bool:
        n = self.node
        if not word:
            return bool(n.d)

        for c in word:
            if n is None:
                return False
            n = n.d.get(c, None)

        return n is not None

    def insert(self, word):
        n = self.node
        for c in word:
            if c in n.d:
                n = n.d[c]
            else:
                n.d[c] = Node()
                n = n.d[c]
        n.end = True