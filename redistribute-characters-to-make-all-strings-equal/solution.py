class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return not any(x % len(words) for x in Counter("".join(words)).values())
