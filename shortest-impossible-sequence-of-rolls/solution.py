class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        now = set()
        steps = 1
        for i in range(len(rolls)):
            now.add(rolls[i])
            if len(now) == k:
                steps += 1
                now = set()
        return steps



