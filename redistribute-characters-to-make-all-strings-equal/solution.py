class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return not any(x % len(words) for x in Counter(letter for word in words for letter in word).values())
