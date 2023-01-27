class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = set(words)
        inconstructible = set()
        constructed = []

        def rec(word: str):
            if word in seen:
                return True
            if word in inconstructible:
                return False
            for i in range(1, len(word)):
                if word[:i] in seen:
                    check = rec(word[i:])
                    if check:
                        seen.add(word)
                        return True
                    else:
                        inconstructible.add(word)
            return False

        for word in words:
            for i in range(1, len(word)):
                if word[:i] not in seen:
                    continue
                if rec(word[i:]):
                    constructed.append(word)
                    break

        return constructed
