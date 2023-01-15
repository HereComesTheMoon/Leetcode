class Node:
    def __init__(self, endpoint: bool):
        self.d: dict[str, "Node"] = {}
        self.endpoint = endpoint

    def __getitem__(self, key: str):
        assert len(key) == 1
        return self.d.get(key, None)

    def insert(self, c: str) -> "Node":
        assert c not in self.d
        assert len(c) == 1
        self.d[c] = Node(False)
        return self.d[c]

        
class Trie:
    def __init__(self):
        self.head = Node(False)

    def insert(self, word: str) -> None:
        par = self.head
        for c in word:
            node = par[c]
            if node is None:
                par = par.insert(c)
            else:
                par = node
        par.endpoint = True

    def search(self, word: str) -> bool:
        par = self.head
        for c in word:
            node = par[c]
            if node is None:
                return False
            par = node
        return par.endpoint

    def startsWith(self, prefix: str) -> bool:
        par = self.head
        for c in prefix:
            node = par[c]
            if node is None:
                return False
            par = node
        return True
        