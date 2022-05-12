class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(x % len(words) == 0 for x in Counter(letter for word in words for letter in word).values())
