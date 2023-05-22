from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        s = list(s)
        s.sort(key=lambda c: (-count[c], c))
        return "".join(s)