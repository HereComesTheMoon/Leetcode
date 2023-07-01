class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for a, b in zip(word1, word2):
            res.append(a)
            res.append(b)
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        res.append(word1[len(word2):])
        return "".join(res)