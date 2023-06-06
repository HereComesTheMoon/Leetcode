class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1_000_000_007
        n = len(words[0])
        m = len(target)
        d = [ [0] * 26 for _ in range(n) ]
        for word in words:
            for k, c in enumerate(word):
                d[k][ord(c) - ord('a')] += 1

        @functools.cache
        def rec(used: int, filled: int) -> int:
            if filled == m:
                return 1
            if (n - used) < (m - filled):
                return 0
            times = d[used][ord(target[filled]) - ord('a')]
            if times == 0:
                return rec(used + 1, filled) 
            else:
                return (times * rec(used + 1, filled + 1) + rec(used + 1, filled)) % MOD

        return rec(0, 0) % MOD