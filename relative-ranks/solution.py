from itertools import chain

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        srted = sorted(score, reverse=True)
        for x, res in zip(srted, chain(["Gold Medal", "Silver Medal", "Bronze Medal"], range(4, len(score) + 1))):
            d[x] = str(res)
        return [ d[x] for x in score ]