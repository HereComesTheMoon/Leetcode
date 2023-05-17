class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = list(sorted(( x - y for x, y in zip(reward1, reward2) ), reverse=True))
        return sum(reward2) + sum(diff[:k])