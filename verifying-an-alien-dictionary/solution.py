class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = { x : k for k, x in enumerate(order) }
        def is_smaller(a: str, b: str) -> bool:
            for i in range(min(len(a), len(b))):
                if a[i] == b[i]:
                    continue
                return d[a[i]] < d[b[i]]
            return len(a) <= len(b)
        
        return all(is_smaller(words[i-1], words[i]) for i in range(1, len(words)))

