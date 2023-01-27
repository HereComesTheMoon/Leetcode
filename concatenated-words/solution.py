class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = set(words)
        constructed = []

        def rec(word: str):
            if word in seen:
                return True
            for i in range(1, len(word)):
                if word[:i] in seen and rec(word[i:]):
                    seen.add(word)
                    return True

        for word in words:
            for i in range(1, len(word)):
                if word[:i] not in seen:
                    continue
                if rec(word[i:]):
                    constructed.append(word)
                    break

        return constructed
