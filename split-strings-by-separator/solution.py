class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return filter(bool, itertools.chain.from_iterable(map(lambda word: word.split(separator), words)))